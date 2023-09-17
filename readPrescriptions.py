# written by Diana Lysova for Pitt Challenge Hackathon
# first version of program greyed out below
# most recent version searches folder for zip files, then reads the images that start with a string of numbers and end in .jpg
# they then get converted into .png images to make them easier to read

import os
import zipfile
import re
from PIL import Image
import io

## my personal file path- will be changed for app
folder_path = "/Users/dianalysova/Downloads/dm_spl_monthly_update_aug2023"

pattern = r'^\d+.*\.jpg$'

for root, dirs, files in os.walk(folder_path):
        
        for file_name in files:
            if file_name.endswith(".zip"):
                zip_file_path = os.path.join(root, file_name)
                

                with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

                    file_list = zip_file.namelist()
                    

                    for file_name in file_list:

                        if re.match(pattern, file_name):

                            with zip_file.open(file_name) as jpg_file:
                                jpg_data = jpg_file.read()
                                # in this step the correct photo is opened and then cross referenced with the data set
                            #(though that code is not in this file, see app.py)

                            with Image.open(io.BytesIO(jpg_data)) as img:

                                png_file_name = re.sub(r'\.jpg$', '.png', file_name, flags=re.IGNORECASE)
                                
                                png_file_path = os.path.join(root, png_file_name)
                                img.save(png_file_path, format='PNG')
                                # this converts the jpg into a png, because tesseract works better with png files
                            
                            print(f"Converted {file_name} to {png_file_name} in {zip_file_path}")
                            
except FileNotFoundError:
    print(f"The specified folder '{folder_path}' was not found.")
except Exception as e:
    print(f"An error occurred, please try again: {e}")


# zip_file_path = "/Users/dianalysova/Downloads/pittChallengeDataSet/prescription.zip"

# try:

  #  with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

   #     file_list = zip_file.namelist()
        
    #    for file_name in file_list:

     #       if re.match(pattern, file_name):

     #           with zip_file.open(file_name) as image_file:
      #              image_data = image_file.read()
                    
                # here the operations are performed and the opened file 
                # from the dataset is cross referenced with the user
                # photo using the ocr tool
                
# except FileNotFoundError:
  #  print(f"The specified zip file '{zip_file_path}' was not found.")
# except Exception as e:
 #   print(f"An error occurred, please try again: {e}")

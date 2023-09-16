# written by Diana Lysova for Pitt Challenge Hackathon


import zipfile
import re

## my personal file path- will be changed for app
zip_file_path = "/Users/dianalysova/Downloads/pittChallengeDataSet/prescription.zip"

pattern = r'^\d+.*\.jpg$'

try:

    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

        file_list = zip_file.namelist()
        
        for file_name in file_list:

            if re.match(pattern, file_name):

                with zip_file.open(file_name) as image_file:
                    image_data = image_file.read()
                    
                # here the operations are performed and the opened file 
                # from the dataset is cross referenced with the user
                # photo using the ocr tool
                
except FileNotFoundError:
    print(f"The specified zip file '{zip_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred, please try again: {e}")

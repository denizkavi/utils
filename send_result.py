import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory_path')
parser.add_argument('zip_file_path')
parser.add_argument('api_key')
args = parser.parse_args()
directory_path = args.directory_path
zip_file_path = args.zip_file_path
key = args.api_key

def create_zip(directory_path, zip_file_path):
    # Create the zip file from the temporary directory
    shutil.make_archive(zip_file_path, 'zip', directory_path)

    print(f'Successfully created zip file: {zip_file_path}')

create_zip(directory_path, zip_file_path)
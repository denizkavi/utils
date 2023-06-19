import os
import shutil
import argparse
import base64 
os.system("pip install sendgrid")
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

parser = argparse.ArgumentParser()
parser.add_argument('directory_path')
parser.add_argument('zip_file_path')
parser.add_argument('api_key')
parser.add_argument('email')
parser.add_argument('jobname')

args = parser.parse_args()
directory_path = args.directory_path
zip_file_path = args.zip_file_path
key = args.api_key
email = args.email
jobname = args.jobname

def create_zip(directory_path, zip_file_path):
    # Create the zip file from the out directory
    shutil.make_archive(zip_file_path, 'zip', directory_path)

create_zip(directory_path, zip_file_path)

##send email of out.zip
message = Mail(from_email='files@tamarind.bio',
               to_emails=email,
               subject=f'Your SignalP 6 Results From Tamarind ({jobname})', #{jobname},
               html_content='See out.zip!')     

message.add_cc("files@tamarind.bio")

with open(f'{zip_file_path}.zip', 'rb') as f:
    data = f.read()
    f.close()
    encoded_file = base64.b64encode(data).decode()
    attachedFile = Attachment(FileContent(encoded_file),FileName(f'{zip_file_path}.zip'),FileType('application/zip'),Disposition('attachment'))
    message.attachment = attachedFile
    sg = SendGridAPIClient(key)
    response = sg.send(message)
import os
import shutil
import argparse

import os
import base64 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

parser = argparse.ArgumentParser()
parser.add_argument('directory_path')
parser.add_argument('zip_file_path')
parser.add_argument('api_key')
parser.add_argument('email')

args = parser.parse_args()
directory_path = args.directory_path
zip_file_path = args.zip_file_path
key = args.api_key
email = args.email

def create_zip(directory_path, zip_file_path):
    # Create the zip file from the out directory
    shutil.make_archive(zip_file_path, 'zip', directory_path)

create_zip(directory_path, zip_file_path)

##send email of out.zip
message = Mail(from_email='files@tamarind.bio',
               to_emails=email,
               subject='Your Structure Prediction From Tamarind',
               html_content='<strong>See out.zip!</strong>')

with open('out.zip', 'rb') as f:
    data = f.read()
    f.close()
    encoded_file = base64.b64encode(data).decode()
    attachedFile = Attachment(FileContent(encoded_file),FileName('out.zip'),FileType('application/zip'),Disposition('attachment'))
    message.attachment = attachedFile
    sg = SendGridAPIClient(key)
    response = sg.send(message)
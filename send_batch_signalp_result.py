import os
import shutil
import argparse
import base64 
os.system("pip install sendgrid")
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

parser = argparse.ArgumentParser()
parser.add_argument('excel_path')
parser.add_argument('api_key')
parser.add_argument('email')
parser.add_argument('jobname')

args = parser.parse_args()
excel_path = args.excel_path
key = args.api_key
email = args.email
jobname = args.jobname

##send email of out.zip
message = Mail(from_email='files@tamarind.bio',
               to_emails=email,
               subject=f'Your SignalP 6 Batch Results From Tamarind ({jobname})', #{jobname},
               html_content='See attached!')     

message.add_cc("files@tamarind.bio")

with open(f'{excel_path}', 'rb') as f:
    data = f.read()
    f.close()
    encoded_file = base64.b64encode(data).decode()
    attachedFile = Attachment(FileContent(encoded_file),FileName(f'{excel_path}'),FileType('application/xlsx'),Disposition('attachment'))
    message.attachment = attachedFile
    sg = SendGridAPIClient(key)
    response = sg.send(message)
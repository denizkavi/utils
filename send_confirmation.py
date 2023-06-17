import argparse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

parser = argparse.ArgumentParser()

parser.add_argument('api_key')
parser.add_argument('email')
parser.add_argument('sequence')

args = parser.parse_args()
key = args.api_key
email = args.email
sequence = args.sequence

##send confirmation email
message = Mail(from_email='files@tamarind.bio',
               to_emails=email,
               subject=f"We've received your sequence. ({sequence})",
               html_content='We will get back to you for the results of the structure prediction soon. Thank you for your using Tamarind!')

message.add_cc("files@tamarind.bio")

sg = SendGridAPIClient(key)
response = sg.send(message)

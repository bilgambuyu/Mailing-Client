#from fileinput import filename
#import imp
import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

#server.login('mail@gmail.com', 'password123')

with open('password.txt', 'r') as f:
    password = f.read()

server.login('billysantos147@gmail.com', password)

#Header & Message Body
msg = MIMEMultipart()
msg['From'] = 'Blacks1de'
msg['To'] = 'bilgambuyu@gmail.com' #Target's email
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
#End Header & Message Body

#Attachment
filename = 'image.png'
attachment = open(filename, 'rb') #rb means Reading Binary

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
#End Attachment

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('billysantos147@gmail.com', 'bilgambuyu@gmail.com', text)
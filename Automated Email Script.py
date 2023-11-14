# Send an automated email using smtplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_email_password"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Automated Email Subject"

body = "Hello, this is an automated email sent using Python!"
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")

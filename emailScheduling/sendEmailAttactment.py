import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = "adityasraj123@gmail.com"
receiver_email = "202001099@daiict.ac.in"
subject = "Email Subject"
body = "This is the email body."

# Attachments
attachment_path = r"C:\Users\adity\Pictures\Screenshots\love.png"  # Replace with the actual path to your file

# Gmail SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 465  # SSL port

# Gmail account credentials (use an App Password if 2FA is enabled)
email_password = "threeSIX9"

# Create a MIME object
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the email body
msg.attach(MIMEText(body, "plain"))

# Attach the file
with open(attachment_path, "rb") as attachment_file:
    base = MIMEBase("application", "octet-stream")
    base.set_payload(attachment_file.read())
    encoders.encode_base64(base)
    base.add_header(
        "Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}"
    )
    msg.attach(base)

# Create a secure SSL context
context = ssl.create_default_context()

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

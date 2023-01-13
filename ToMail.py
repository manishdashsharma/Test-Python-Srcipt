import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "lucifer25gaming@gmail.com"
email_password = "wcxuailiemwstzfk"

def mail(subject,to,message_content):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    msg.set_content(message_content)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
    return f"Mail has been been sent {to}"
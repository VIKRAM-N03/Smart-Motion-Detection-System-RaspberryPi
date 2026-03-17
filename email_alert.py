import smtplib
from email.message import EmailMessage

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
TO_EMAIL = "receiver_email@gmail.com"

def send_email(image_path):
    msg = EmailMessage()
    msg['Subject'] = '🚨 Motion Detected'
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content("Motion detected! See attached image.")

    with open(image_path, 'rb') as f:
        img = f.read()
        msg.add_attachment(img, maintype='image', subtype='jpeg', filename='image.jpg')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print("Email sent!")
import smtplib, ssl
from PASSWORD import PASSWORD

def send_email(message):
    username = "krutezashka@gmail.com"
    password = PASSWORD

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
import smtplib,ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "databasewarehouae@gmail.com"
    password = os.environ.get("password")
    receiver = "kojibello058@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    return None


if __name__ == "__main__":
    pass

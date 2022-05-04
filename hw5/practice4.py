import smtplib
from email.message import EmailMessage
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content('잘 부탁드립니다.')

message["Subject"] = "저는 천승범입니다!"
message["From"] = "0921sean@gmail.com"
message["To"] = "ksjoon28@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("0921sean@gmail.com", "#####")
# 비밀번호는 가렸습니다.
sendEmail("ksjoon28@naver.com")
smtp.quit()
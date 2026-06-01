import datetime as dt
import random
import smtplib
import pandas
import os 

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def send_birthday_email(name,to_email):
    letter_number = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        letter_content = letter_file.read()
        updated_letter_content = letter_content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Happy Birthday!!!\n\n{updated_letter_content}")

data = pandas.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient="records")

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day
today = (current_month, current_day)

for person in birthday_list:
    birthday_month = person["month"]
    birthday_day = person["day"]
    birthday = (birthday_month,birthday_day)
    if birthday == today:
        send_birthday_email(name=person["name"], to_email=person["email"])




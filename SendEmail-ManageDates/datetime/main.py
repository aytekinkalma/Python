# import smtplib
#
#
# my_email="kalma.aytekin@gmail.com"
# password="******"
# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="whıch adrees to send message",msg="Subject:Hello\n\nThis is the body of my email./")
# connection.close()

# import datetime as dt
# now=dt.datetime.now()
# month=now.month
# day_of_week=now.weekday()
# year=now.year
# date_of_birth=dt.datetime(year=1994,month=12,day=10)
# print(date_of_birth)
import random
import  smtplib
import datetime as dt

my_email="kalma.aytekin@gmail.com"
my_password="******"


now=dt.datetime.now()
weekday=now.weekday()
if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.co") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday Motivation\n\n{quote}")
        

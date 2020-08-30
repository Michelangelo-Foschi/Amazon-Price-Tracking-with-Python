import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.ae/LEGO-Ideas-International-Station-21321/dp/B0844WLH35/ref=sr_1_1?dchild=1&keywords=lego+iss&qid=1598777217&sr=8-1'

headers = {"User-Agent": 'YOUR USER AGENT'}

def check_price():

    page = requests.get(URL, headers=headers) #returns data from website

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[3:7])

    if(converted_price < YOUR PREFERRED PRICE):
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR EMAIL ADDRESS', 'YOUR GENERATED APP PASSSWORD')

    subject = 'Price fell down for your Lego ISS'
    body = 'Check the amazon link https://www.amazon.ae/LEGO-Ideas-International-Station-21321/dp/B0844WLH35/ref=sr_1_1?dchild=1&keywords=lego+iss&qid=1598777217&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'SENDERS EMAIL',
        'RECEIVERS EMAIL',
        msg
    )
    print('Mail sent')
    server.quit()
check_price()

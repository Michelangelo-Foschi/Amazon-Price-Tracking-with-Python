
# Amazon-Price-Tracking-with-Python

You probably have hundreds of things you would like to buy on Amazon, but sometimes they are just too expensive and the worse thing about it, it’s that you could be missing out hundreds of short-term offers! 

Now let’s get this problem solved by writing an easy and short python script, that sends you an email, whenever the price goes down.

## **Requirements:**
- Amazon’s URL of your preferred item
- Your User-Agent, which can be found by going on your default web browser and searching for “My user agent”
- A Gmail account
- Two-step verification turned on. -> Go on your google account (Manage Account) -> Security (On the left side of the navigation bar) -> Signing into Google -> Set up 2-Step verification

## **Python Package Installation:**
- We only need to install one package, which is called requests.
- Code: Pip Install requests bs4
- “Requests” helps us to retrieve data from any website.

## **Importing Packages:**
``` python
import requests
from bs4 import BeautifulSoup
import smtplib
```
- "smtplib" is needed to give us the function to send emails.

## **Code Setup:**
``` python
URL = ‘Your item’s URL’
headers = {“User-Agent”: ‘Your User-Agent’}
```
## **Check Price function:**
``` python
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
```
  - Things that could be different in your case:
    - The title id -> To look up your title id go on your amazon item’s URL and highlight the title. Then right-click and open the “inspect element” function. Once                    the inspector is opened you will get a line of code highlighted. Search for the keyword “id” and copy your item’s id. In my case, the id is “productTitle”.
    - The price id -> To look up your price id go on your amazon item’s URL and highlight the title. Then right-click and open the “inspect element” function. Once the inspector is opened you will get a line of code highlighted. Search for the keyword “id” and copy your item’s id. In my case, the id is “price block_ourprice”.

## **Send Mail Function:**
- Now before starting to type this send_mail function let’s create our generated password. Once you have turned on your 2-step verification, you can head back to the security navigation page. Under signing-in to Google, you see a tab called App passwords. Now click on this tab. Under “Select App” select the option “Mail” and under “Select device” select the device you are doing this project on. In my case, I would choose the option “Mac”. Then click generate.
Now we have our generated password.

``` python 
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
```

## **Call Our Function:**
``` python
check_price()
```
## **Code Recap:**
- Notice: You could be also willing to change your preferred price number, instead of 330.0. & maybe you would also want to change the converted_price, instead of "[3:7].

# **END:**
- Hopefully this tutorial helped you in solving this tricky, but important problem. As this is my first story I publish, I would like to hear from you what you think about this publishing.
Thanks and stay safe!

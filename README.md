# Amazon-Price-Tracking-with-Python
You probably have hundreds of things you would like to buy on Amazon, but sometimes they are just too expensive and the worse thing about it, it’s that you could be missing out hundreds of short-term offers! 

Now let’s get this problem solved by writing an easy and short python script, that sends you an email, whenever the price goes down.

Requirements:
- Amazon’s URL of your preferred item
- Your User-Agent, which can be found by going on your default web browser and searching for “My user agent”
- A Gmail account
- Two-step verification turned on. -> Go on your google account (Manage Account) -> Security (On the left side of the navigation bar) -> Signing into Google -> Set up 2-Step verification

Python Package Installation:
- We only need to install one package, which is called requests.
- Code: Pip Install requests bs4
- “Requests” helps us to retrieve data from any website.

Importing Packages
- Code: import requests
- Code: from bs4 import BeautifulSoup
- Code: import smtplib
- smtplib is needed to give us the function to send emails.

Code Setup
- Code: URL = ‘Your item’s URL’
- Code: headers = {“User-Agent”: ‘Your User-Agent’}

Check Price function
  - Things that could be different in your case:
    - The title id -> To look up your title id go on your amazon item’s URL and highlight the title. Then right-click and open the “inspect element” function. Once                    the inspector is opened you will get a line of code highlighted. Search for the keyword “id” and copy your item’s id. In my case, the id is “productTitle”.
    - The price id -> To look up your price id go on your amazon item’s URL and highlight the title. Then right-click and open the “inspect element” function. Once the inspector is opened you will get a line of code highlighted. Search for the keyword “id” and copy your item’s id. In my case, the id is “price block_ourprice”.


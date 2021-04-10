import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/dp/B08HRZ3MXK/?coliid=I177TXU916CDMC&colid=TCREPSQAB6YM&psc=1&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    formatPrice = float(price.split()[1].replace(',',''))
    # print(formatPrice)
    # print(title.strip())

    if formatPrice<1199:
        send_mail(title)

def send_mail(title):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # ...send emails

        
        server.login('akhilrob2@gmail.com','jqvjeiqheojvlzsa')
        
        subject = 'Price Fell Down!'
        body = f'Check the amazon link {url} for {title}'
        msg = f'Subject: {subject}\n\n{body}'
        
        server.sendmail(
            'akhilrob2@gmail.com',
            'akhildaphara@gmail.com',
            msg
        )
        print('An email was sent')
    except Exception as e:
        print('Something went wrong: ' + e)
    
    server.quit()
    
while True:
    check_price()
    time.sleep(60*60*4)
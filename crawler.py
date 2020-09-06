# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:52:33 2020

@author: wechyu88
"""
url='https://movie.douban.com/' #需要爬数据的网址
date="20200702"

sleepTime=900#seconds
url2="https://wwws.airfrance.us/search/offers?pax=1:0:0:0:0:0:0&cabinClass=ECONOMY&activeConnection=0&connections=CDG:A:"+date+"%3EPVG:A&bookingFlow=LEISURE"


from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


#qq邮箱smtp服务器
mail_host = 'smtp.163.com'  
#163用户名
mail_user = 'wencheng2961188'  
#密码(部分邮箱为授权码) 
mail_pass = 'MAshaoze#001'   
#邮件发送方邮箱地址
sender = 'wencheng2961188@163.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['wencheng2961188@gmail.com']  


#headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#         'referer': 'https://wwws.airfrance.us/search/offers?pax=1:0:0:0:0:0:0&cabinClass=ECONOMY&activeConnection=0&connections=CDG:A:20200924%3EPVG:A&bookingFlow=LEISURE',
#         'cookie': 'optimizelyEndUserId=oeu1592944597599r0.5133573727922776; af_gdpr=1; _svtri=0061f77b-3498-4952-b1dd-82bc3884b81f; _ga=GA1.2.563786295.1592944601; wzuid=74874eda5ef267d8; _gcl_au=1.1.1242493328.1592944601; __troRUID=9d816cb8-380e-44e6-bf11-fdbe51a8de16; _gac_UA-44698027-5=1.1593013811.CjwKCAjw88v3BRBFEiwApwLevZwX9Ndfxac46tqWX5VHpv0Ye1T-Da6uUXdCSw6U1bwGemJ6igNDFxoCfX4QAvD_BwE; _gcl_dc=GCL.1593013812.CjwKCAjw88v3BRBFEiwApwLevZwX9Ndfxac46tqWX5VHpv0Ye1T-Da6uUXdCSw6U1bwGemJ6igNDFxoCfX4QAvD_BwE; _gcl_aw=GCL.1593013812.CjwKCAjw88v3BRBFEiwApwLevZwX9Ndfxac46tqWX5VHpv0Ye1T-Da6uUXdCSw6U1bwGemJ6igNDFxoCfX4QAvD_BwE; bm_sz=2310133F9223B8D96B391343FF7AB894~YAAQT+4uFwd0i99yAQAAw0Gw7AjyGsYS98fsJu68tQWEN9zs0YYngsyWor7lv+hG/4aKk+b5G9WpXprl3tpH19fCTY3JDxvFABGMIsupfH3baOh64mmlodz52Ne01nOVl2xPGseII+WW1dBEUOYS9oskkF9HmmPQVQJVxDV7Llkh9OUOxzE/k9FfdEb0n9QbcOo=; _gid=GA1.2.1355262936.1593108875; AFKL_VISITOR_ID=1959845960121530; af_marketcode_parent=US; klm_tracking_id=23136838_10.60.2.47; _svlet=1593109361215; klm_tracking_id=23136838_10.60.2.47; secure_aviato_id=s%3A8ed5b561-f433-4d19-9607-619f9bd5ec27.IAvFKqoZGUKGMKZzUMi178YanPna97IzDPIkMunJZb8; _csrf=foCH2QBE0tq5pt_8QASVa563; __troSYNC=1; ESVSS=e6d2f3bc; ESVTRK=74874eda5ef267d8||3bcbd7695ef5054b; ak_bmsc=480C182F3254B68E5D64AA26211AEEBE17373937837E00007808F55E50F5D178~plM+NHGx3w8+SJ+FTanIUxZy4R86NhGa85bUyMTXHTphSkJGYJ/B6EZrLtOE85kfyLYxEoKzdKY4ldiNN7Fzq6oYSsWmA1466STR5t8P+g/jFVHdWOqaEDsApc76MzEQ9a32swwxx7GbYwzuovetnG+52DG0jAAJuHz0bP2gkIOEB8IHli2eCNTiyXPD+TFqWwLZ8s1ej2cUtOKym7z7qmx0ui1P6IcO09UZASLVyK6aaVkPX3ATtkiG2d1B/QuI2R; _svs=%7B%22c%22%3A%7B%221%22%3Atrue%2C%222%22%3Atrue%2C%223%22%3Atrue%7D%2C%22ct%22%3A1592944600820%2C%22p%22%3A%7B%227%22%3A1593115979672%2C%2212%22%3A1593116795495%2C%223002%22%3A1593115979658%2C%224242%22%3A1593114328533%7D%2C%22m%22%3A%7B%22adblocktest%22%3A%7B%22adblocktest%22%3A1595536600836%7D%7D%7D; _svlet=1593116795500; _gat=1; __trossion=1592944724_1800_3_9d816cb8-380e-44e6-bf11-fdbe51a8de16%3A1593109375_9d816cb8-380e-44e6-bf11-fdbe51a8de16%3A1593114329_1593116795_7_; _uetsid=53a07188-b552-323e-d001-01e8471e4082; _uetvid=cfbd3f2d-b888-ac75-6e7d-b45a38e0d338; QSI_AFKLM_PageCount=8; XSRF-TOKEN=7kW4UX9W-099GdSTgBeWJEoBb2YKms2kHBFU; bm_sv=0FA75E972127468E214D36947A52B67A~o3zNwtkRIw05l4XO4c65oJtxKJ4BRxWLwDy/GISCapD1LjB8yrTXSqT4NYRJ3tRD8q1K9CYUlC4nTpSjLo3cPUS9Mhpq8rOKB9IWCcF9sue7nqAaF4745VkN7pEh35Dy9dMgmRsRye5Za/rSyRxqi3eQkorfzAcTZ7qMLeSi2/E=; _abck=1818C9745E6F27EB474E6150F6FAB172~-1~YAAQNzk3F0YaduZyAQAAgeMp7QTdeHcvsIZmz78w7HGOmGIvfkiofi04Jq0VYWEHEYHSsl3CAtO3g2dSWhN6XTUX3yvSjsvncqcQydDPtcW+f5xZZM/A9Mcdsvs/OUfdImjKQ18+xX2D2t9xB+6SUj6ujwMNEclAIhz21yERPl2TFFBxWbRnCclREKagLBcJIFuRoqx/Kt8iWbGYi9NgsxJQWQBa+Ug0U5+Zjllxx9bZnsCMmRgRj3TpxDOcgW1xzZS30Cok0y9SGzl1NHUwPGAQ2D237xR80ppvOLR5RkAHA6/de5h1WntDtHPhuJYmO0pkiObt3k4A~0~-1~-1'
#        }


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Cookie": "optimizelyEndUserId=oeu1592944597599r0.5133573727922776; af_gdpr=1; _svtri=0061f77b-3498-4952-b1dd-82bc3884b81f; _ga=GA1.2.563786295.1592944601; wzuid=74874eda5ef267d8; _gcl_au=1.1.1242493328.1592944601; __troRUID=9d816cb8-380e-44e6-bf11-fdbe51a8de16; _gac_UA-44698027-5=1.1593013811.CjwKCAjw88v3BRBFEiwApwLevZwX9Ndfxac46tqWX5VHpv0Ye1T-Da6uUXdCSw6U1bwGemJ6igNDFxoCfX4QAvD_BwE; _gcl_dc=GCL.1593013812.CjwKCAjw88v3BRBFEiwApwLevZwX9Ndfxac46tqWX5VHpv0Ye1T-Da6uUXdCSw6U1bwGemJ6igNDFxoCfX4QAvD_BwE; _gcl_aw=GCL.1593013812.CjwKCAjw88v3BRBFEiwApwLevZwX9Ndfxac46tqWX5VHpv0Ye1T-Da6uUXdCSw6U1bwGemJ6igNDFxoCfX4QAvD_BwE; bm_sz=2310133F9223B8D96B391343FF7AB894~YAAQT+4uFwd0i99yAQAAw0Gw7AjyGsYS98fsJu68tQWEN9zs0YYngsyWor7lv+hG/4aKk+b5G9WpXprl3tpH19fCTY3JDxvFABGMIsupfH3baOh64mmlodz52Ne01nOVl2xPGseII+WW1dBEUOYS9oskkF9HmmPQVQJVxDV7Llkh9OUOxzE/k9FfdEb0n9QbcOo=; _gid=GA1.2.1355262936.1593108875; AFKL_VISITOR_ID=1959845960121530; af_marketcode_parent=US; klm_tracking_id=23136838_10.60.2.47; _svlet=1593109361215; klm_tracking_id=23136838_10.60.2.47; secure_aviato_id=s%3A8ed5b561-f433-4d19-9607-619f9bd5ec27.IAvFKqoZGUKGMKZzUMi178YanPna97IzDPIkMunJZb8; _csrf=foCH2QBE0tq5pt_8QASVa563; __troSYNC=1; ESVSS=e6d2f3bc; ESVTRK=74874eda5ef267d8||3bcbd7695ef5054b; ak_bmsc=480C182F3254B68E5D64AA26211AEEBE17373937837E00007808F55E50F5D178~plM+NHGx3w8+SJ+FTanIUxZy4R86NhGa85bUyMTXHTphSkJGYJ/B6EZrLtOE85kfyLYxEoKzdKY4ldiNN7Fzq6oYSsWmA1466STR5t8P+g/jFVHdWOqaEDsApc76MzEQ9a32swwxx7GbYwzuovetnG+52DG0jAAJuHz0bP2gkIOEB8IHli2eCNTiyXPD+TFqWwLZ8s1ej2cUtOKym7z7qmx0ui1P6IcO09UZASLVyK6aaVkPX3ATtkiG2d1B/QuI2R; _svs=%7B%22c%22%3A%7B%221%22%3Atrue%2C%222%22%3Atrue%2C%223%22%3Atrue%7D%2C%22ct%22%3A1592944600820%2C%22p%22%3A%7B%227%22%3A1593115979672%2C%2212%22%3A1593116795495%2C%223002%22%3A1593115979658%2C%224242%22%3A1593114328533%7D%2C%22m%22%3A%7B%22adblocktest%22%3A%7B%22adblocktest%22%3A1595536600836%7D%7D%7D; _svlet=1593116795500; _gat=1; __trossion=1592944724_1800_3_9d816cb8-380e-44e6-bf11-fdbe51a8de16%3A1593109375_9d816cb8-380e-44e6-bf11-fdbe51a8de16%3A1593114329_1593116795_7_; _uetsid=53a07188-b552-323e-d001-01e8471e4082; _uetvid=cfbd3f2d-b888-ac75-6e7d-b45a38e0d338; QSI_AFKLM_PageCount=8; XSRF-TOKEN=7kW4UX9W-099GdSTgBeWJEoBb2YKms2kHBFU; bm_sv=0FA75E972127468E214D36947A52B67A~o3zNwtkRIw05l4XO4c65oJtxKJ4BRxWLwDy/GISCapD1LjB8yrTXSqT4NYRJ3tRD8q1K9CYUlC4nTpSjLo3cPUS9Mhpq8rOKB9IWCcF9sue7nqAaF4745VkN7pEh35Dy9dMgmRsRye5Za/rSyRxqi3eQkorfzAcTZ7qMLeSi2/E=; _abck=1818C9745E6F27EB474E6150F6FAB172~-1~YAAQNzk3F0YaduZyAQAAgeMp7QTdeHcvsIZmz78w7HGOmGIvfkiofi04Jq0VYWEHEYHSsl3CAtO3g2dSWhN6XTUX3yvSjsvncqcQydDPtcW+f5xZZM/A9Mcdsvs/OUfdImjKQ18+xX2D2t9xB+6SUj6ujwMNEclAIhz21yERPl2TFFBxWbRnCclREKagLBcJIFuRoqx/Kt8iWbGYi9NgsxJQWQBa+Ug0U5+Zjllxx9bZnsCMmRgRj3TpxDOcgW1xzZS30Cok0y9SGzl1NHUwPGAQ2D237xR80ppvOLR5RkAHA6/de5h1WntDtHPhuJYmO0pkiObt3k4A~0~-1~-1"
}

from selenium import webdriver
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
chrome_driver = "C:\\Users\\wechyu88\\eclipse-workspace\\MyCrawLer\\chromedriver"

driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
#path = r'C:\\Users\\wechyu88\\eclipse-workspace\\MyCrawLer\\chromedriver'
#driver = webdriver.Chrome(executable_path = path,chrome_options=chrome_options)

from datetime import datetime



def sendMessage(message):
    mail_host = 'smtp.163.com'  
    #163用户名
    mail_user = 'wencheng2961188'  
    #密码(部分邮箱为授权码) 
    mail_pass = 'MAshaoze#001'   
    #邮件发送方邮箱地址
    sender = 'wencheng2961188@163.com'  
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['wencheng2961188@gmail.com']  
    
    
    message = MIMEText(message,'plain','utf-8')
    #邮件主题       
    message['Subject'] = 'title' 
    #发送方信息
    message['From'] = sender 
    #接受方信息     
    message['To'] = receivers[0]  
    
    try:
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        #退出
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误

def retrieve(url2):
    driver.get(url2)
    try:    
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cookiebarAgreeContent"]/button[2]'))
        )
        randomWaiting=random.random()*1+1
        time.sleep(randomWaiting)
        element.click()
    except:
        print("no cookie agree button")
    sorryOrNot='NoSorry'
    try:
        noseatpath='//*[contains(@class,"bwc-notification__main")]//*[contains(@class,"bwc-o-body-variant")]'
        noseatOrNot = driver.find_element_by_xpath(noseatpath)
        sorryOrNot = noseatOrNot.text.split(' ')[0]
        print(sorryOrNot)
    except:
        sorryOrNot = 'NoSorry'

    AvSeatspath='//*[contains(@class,"bw-itinerary-seats-left")]'
    leftCount='0'
    try:   
        leftseat = driver.find_element_by_xpath(AvSeatspath)
        leftCount = leftseat.text.split(' ')[0]
    except:
        leftCount ='0'

    #leftCount = 'GreaterThan Zero'
    if(sorryOrNot!='NoSorry'):
        leftCount='0'
    return leftCount


leftCount='0'
while leftCount == '0':
    randomWaiting=random.random()*5+sleepTime
    time.sleep(randomWaiting)
    leftCount=retrieve(url2)
    now = datetime.now()
    if(leftCount!='0'):
        sendMessage(date+" find "+ leftCount+" seats "+str(now))
    print(date+" find "+leftCount+" seats :"+str(now))
    
    #driver.find_element_by_xpath('//*[@id="cookiebarAgreeContent"]/button[2]').click()

#driver.find_element_by_xpath('/html/body/bw-app/bwc-page-template/mat-sidenav-container/mat-sidenav-content/div/main/div/bw-search-result-container/div/div/section/bw-flight-lists/bw-flight-list-result-section/section/bw-itinerary-list/ol/li/bw-itinerary-row/div/div/div[2]/bw-itinerary-seats-left/div')
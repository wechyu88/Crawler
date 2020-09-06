# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:37:25 2020

@author: wechyu88
"""

#! /usr/bin/env python
#coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


#qq邮箱smtp服务器

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
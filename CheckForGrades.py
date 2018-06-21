import time
import smtplib
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass
un = getpass.getpass('Enter Username:')
pw = getpass.getpass('Enter password:')
id0 = getpass.getpass('Enter ID:')
print('[Successfuly Insterted]')

#email credentials
un1 = getpass.getpass('Enter your Gmail:')
pw1 = getpass.getpass('Enter password:')
print('[Successfuly Insterted]')
print('Script Running...')
#autoLogin to gezer

browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
browser.get('https://gezer1.bgu.ac.il/meser/login.php')
time.sleep(5)
email = browser.find_element_by_css_selector('#username').send_keys(un)
password = browser.find_element_by_css_selector('#pass')
password.send_keys(pw)
iD = browser.find_element_by_css_selector('#id')
iD.send_keys(id0)
sign = browser.find_element_by_css_selector('#mainContent > form > input')
sign.click()
time.sleep(2)
accept = browser.find_element_by_css_selector('body > form > div.HTable > div > div:nth-child(1) > input')
time.sleep(2)
accept.click()

#auto refresh 
def checkforupdates():
    isExist = browser.page_source.__contains__(time.strftime("%d/%m"))
    if(isExist):
        return True
    else:
        time.sleep(30)
        browser.refresh()
        print ('Last Check: ' + time.ctime())
        print(time.strftime("%d/%m"))
        checkforupdates()

#send_email function
def send_email(user, pwd, recipient, subject):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient
    message = subject
    try:
        #send mail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()

        #send message
        print '### Grades Uploaded Successfuly, Check your mail ###'
    except:
        print "incorrect password or username"
#main function
def main():
    if(checkforupdates()):
        #send_email(un1,pw1,un1,"Grades Uploaded Succesfuly")
        send_email(un1,pw1,un1,"Grades Uploaded")     
main()

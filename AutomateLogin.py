###07/12/2018
###Author: Pratik Sanghvi
###Automate login to Uwindsor Gmail,BlackBoard,Facebook

#GeckoDriver is a prerequisite for running firefox using selenium.
from selenium import webdriver
#import selenium.webdriver.support.ui as ui
import time
#getPass package to hide the characters while typing the password
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging as log
from selenium.webdriver.firefox.options import Options

log.basicConfig(level=log.INFO)

#accept the user name and password for UwinMail,Facebook.
uwinMail = input('Uwin maild >')
uwinUsername = input('username for uwindsor >')
uwinPass = getpass('Password for uwindsor >')
fbUsername = input('username for facebook >')
fbpass = getpass('Password for Facebook >')

log.info('1. Details recorded for logging into Uwindsor and Facebook.')

#disable the web notifications and open the browser
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
browser = webdriver.Firefox(firefox_options=options)

log.info('2. Firefox browser opened')

#open gmail
browser.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
log.info('3. Opening Gmail')

#set the mail id field with the value of the variable uwinMail..
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys(uwinMail)

#click on the next button to move to the password screen
browser.find_element_by_class_name('RveJvd.snByac').click()

#set the username input field with the value of uwinUsername.
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(uwinUsername)

#set the password field with uwinPass.
browser.find_element_by_id('password').send_keys(uwinPass)

#click on the next button to login to gmail account
browser.find_element_by_class_name('form-element.form-button').click()
log.info('4. Login to gmail')

#login for blackboard
#open blackboard  website in new tab
browser.execute_script("window.open('https://blackboard.uwindsor.ca/')")

log.info('5. open blackboard')

#swithc focus of browser to second tab with the blackboard website
browser.switch_to.window(browser.window_handles[1])

#wait unitl the Login button loads
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'casUrl'))).click()
log.info('6. Login to blackboard')

#open facebook in new tab
browser.execute_script("window.open('https://www.facebook.com/')")
log.info('7. Open facebook')

#switch the browser focus to the new open window
browser.switch_to.window(browser.window_handles[2])

#wait for the email field to load and populate it with contents of fbUsername
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(fbUsername)

#iset the value of password with the contents of fbpass
browser.find_element_by_id('pass').send_keys(fbpass)

#click on the login button
browser.find_element_by_id('loginbutton').click()
log.info('8. Login to facebook')

#search for the udemy free coupons group
browser.find_element_by_class_name('_1frb').send_keys('Udemy FREE Coupons, New Launches, FREE Courses')

#click on the search button
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, '_42ft._4jy0._4w98._4jy3._517h._51sy'))).click()
###08/12/2018
###Author: Pratik Sanghvi
###Play game 2048

from selenium import webdriver
import logging as log
import time
from selenium.webdriver.common.keys import Keys

log.info("1.Open the website")
#open the Firefox browser
browser = webdriver.Firefox()

#get the website of the 2048 game
browser.get('https://gabrielecirulli.github.io/2048/')

#wait for the site to load
time.sleep(2)

#get the html element to later send keystrokes to the browser
htmlElem = browser.find_element_by_tag_name('html')

#send keystrokes until game is over
while browser.find_element_by_class_name('retry-button').is_displayed != True:
	log.info("before up")
	htmlElem.send_keys(Keys.UP)
	log.info("before down")
	htmlElem.send_keys(Keys.DOWN)
	log.info("before left")
	htmlElem.send_keys(Keys.LEFT)
	log.info("before right")
	htmlElem.send_keys(Keys.RIGHT)
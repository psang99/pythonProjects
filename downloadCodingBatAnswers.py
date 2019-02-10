###16/12/2018
###Author: Pratik Sanghvi
### Script to download my solutions from coding Bat website for java category.


from selenium import webdriver
import logging as log
import time
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests, os, bs4

username = input('Enter mail id for login\n>>>')

pw = getpass('Enter password\n >>>')

#open the Firefox browser
browser = webdriver.Firefox()

#open the coding bat website in browser
browser.get('https://codingbat.com/java')

dirName=".\CodingBatSolution"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")
	
os.chdir(dirName)
root = os.getcwd()


#waiting for the user name box and setting it to the specific username
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,'uname'))).send_keys(username)

#waiting for the password field and setting it to the entered password
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,'pw'))).send_keys(pw)

#Wait for the login button and click on it
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,'dologin'))).click()

#get the html code of the current page in the browser
problems = browser.page_source

#parse the html using BeautifulSoup
soup = bs4.BeautifulSoup(problems,"lxml")

#select the list of problem categories from the given element
problemCategories = soup.select('div.tabin div:nth-of-type(1)')

#select all the links from the table
solvedCategories = problemCategories[0].select('a')

#iterate over each problem categories
for categoryLink in solvedCategories:

	os.chdir(root)

	temp=categoryLink.get('href')
	dirName = temp[temp.rfind("/")+1 :]
	
	if not os.path.exists(dirName):
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ")
	else:    
		print("Directory " , dirName ,  " already exists")
		
	os.chdir(dirName)
	
	#get the webpage of all the categories of the first page
	browser.get('https://codingbat.com/'+categoryLink.get('href'))
	
	#Parse the html content and extract the categories
	solutionPageList = bs4.BeautifulSoup(browser.page_source,'lxml')
	
	#get all the elements of the table tage inside div.indent
	solutionPageElement = solutionPageList.select('div.indent table')
	
	
	#loop over all the given problems
	for problemLink in solutionPageElement[0].select('a'):
		#select the link
		solutionLink = problemLink.get('href')
		
		#open the webpage with that link
		browser.get('https://codingbat.com/'+solutionLink)

		#get the html content of the opened web page
		solutionText = bs4.BeautifulSoup(browser.page_source,'lxml')

		#get the solution for the problem
		solutionText1 = solutionText.select('div.ace_scroller > div.ace_content > div.ace_layer.ace_text-layer')
		
		#get the problem name
		problemName = solutionText.select('div.indent > span.h2')
		f = open("C:\\Pratik\\GitRepo\\pythonProjects\\CodingBatSolution\\"+dirName+"\\"+problemName[0].text+".java","w+")
		f.write(solutionText1[0].text)

		f.close()
	os.system("cd ..")
	
#log out from the website	
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH,'//a[text()="log out"]'))).click()

#close the browser
browser.quit()
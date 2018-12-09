###12/05/2018
###Author:Pratik Sanghvi
###Searches the address from clipboard or the command line in google map.

import webbrowser,sys,pyperclip

mapUrl='https://www.google.com/maps/place/'

if len(sys.argv) > 1:
	#Get address from the command line
	address = ' '.join(sys.argv[1:])
	print(address)
else:
	#Get the contents of the clipboard
	address = pyperclip.paste()


#open the Google map in the default web browser and search the webpage
#new = 2 opens the website in the new tab
webbrowser.open(mapUrl+address,new=2)
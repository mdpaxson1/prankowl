# must add chrome driver to PATH

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import ConfigParser
import time
import argparse



class redditConfig:
	def __init__(self, numbers, visibleBrowser=0):
		self.numbers = numbers
		self.visibleBrowser = visibleBrowser #0 or 1

class BrowserBot:


	def __init__(self, visibilty, url):

		# make it a headless driver
		self.display = Display(visible=visibility, size=(800, 600))
		self.display.start()

		self.driver = webdriver.Chrome()
		print "driver started"
		self.url = url


		print "Navigating to: " + url
		self.driver.get(url)


	#
	#
	def dislikeComment(self, cssIdentifier):

		elem_dislike_btn = self.driver.find_element_by_id("number1")
		#click first to remove placeholder text
		elem_num1.click()
		elem_num1.send_keys(number1)

		time.sleep(40)
		self.display.stop()





#parser is already defined
#returns configured ArgeParser object
def commandlineArguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("-c1", "--c1", help="country code for first number")
	parser.add_argument("-n1", "--n1", help="#number to call 1")
	parser.add_argument("-ci1", "--ci1", help="# caller id1's country code")
	parser.add_argument("-id1", "--id1", help ="# caller id for number1")
	parser.add_argument("-c2", "--c2", help="# country code for second number")
	parser.add_argument("-n2", "--n2", help="# number for the second number")
	parser.add_argument('-ci2', "--ci2", help="# country coude for id2")
	parser.add_argument("-id2", "--id2", help="# caller id for nuber 2")
	parser.add_argument("-v", "--v", help="#visible browser (1:True 0:")
	args = parser.parse_args()

	if args.c1 == None:
		args.c1 = 1
	if args.ci1  == None:
		args.ci1 = 1
	if args.c2 == None:
		args.c2 = 1
	if args.ci2 == None:
		args.ci2 = 1
	if args.v == None:
		args.v == 0

	if args.n1 == None or args.n2 == None:
		print "-c1 \tcountry code for number1 (default 1)"
	 	print "-n1 \tnumber1 to call without country code"
		print "-ci1 \tcountry code for caller id1 (default1)"
		print "-id1 \tcaller id for number 1 "

		print "-c2 \tcountry code for number2 (default 1)"
		print "-n2 \tnumber2 to make number1 call without country code"
		print "-ci2 \tcountry code for callerid 2 (default1)"
		print "-id2 \tcaller id for number2"
		print "-v  \t 1:Visible 0:Invisible browser (0 is default)"
		print "-h \tfor help"

	return args





if __name__ == "__main__":
	## argsparse numbers
	secondsInDay = 86400
	args = commandlineArguments()
	browser = BrowserBot(args.v) #args.v = visibility

	browser.operatorPrank(args.c1, args.n1, args.ci1, args.id1, args.c2, args.n2, args.ci2, args.id2)


	#while (True):
	#	callPeople()
	#	time.sleep(secondsInDay)

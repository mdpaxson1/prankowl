# must add chrome driver to PATH

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import config
import time

class SeleniumStuff:
	def __init__(self, url ):

		# make it a headless driver
		self.display = Display(visible=config.visibleBrowser, size=(800, 600))
		self.display.start()

		self.driver = webdriver.Chrome()
		print "driver started"
		self.url = url

		print "Navigating to: " + url
		self.driver.get(url)

	def operatorPrank(self, cc1, number1, id1, cc2, number2, id2):

		print "Number1: " + str(cc1) + str(number1) + "    Caller ID 1: " + str(id1)

		print "Number2: " + str(cc2) + str(number2) + "    Caller ID 2: " + str(id2)

		#elem_num1_country = self.driver.find_element_by_id("number1_country")
		#elem_num1_country.send_keys(cc1)


		elem_num1 = self.driver.find_element_by_id("number1")
		#click first to remove placeholder text
		elem_num1.click()
		elem_num1.send_keys(number1)

		elem_id1 = self.driver.find_element_by_id("callerid1")
		#click first to remove placeholder text
		elem_id1.click()
		elem_id1.send_keys(id1)

		#elem_id1_country = self.driver.find_element_by_id("callerid1_country")
		#elem_id1.send_keys(cc1)

		elem_num2  = self.driver.find_element_by_id("number2")
		#click first to remove placeholder text
		elem_num2.click()
		elem_num2.send_keys(number2)

		elem_id2 = self.driver.find_element_by_id("callerid2")
		#click first to remove placeholder text
		elem_id2.click()
		elem_id2.send_keys(id2)

		#press the submit button
		elem_submit = self.driver.find_element_by_id("submit")
		elem_submit.click()



def callPeople():
	counter = 0
	while counter < 3: # you are give 3 credits in a day
		url = 'http://www.prankowl.com/#operatorprank'
		sel = SeleniumStuff(url)

		num1 = random.choice(config.numbers)
		num2 = random.choice(config.numbers)
		id1 = random.choice(config.numbers)
		id2 = random.choice(config.numbers)

		sel.operatorPrank(1, num1, id1, 1, num2, id2)
		counter+=1
		time.sleep(120)






if __name__ == "__main__":
	secondsInDay = 86400
	while (True):
		callPeople()
		time.sleep(secondsInDay)

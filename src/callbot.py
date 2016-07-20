# must add chrome driver to PATH

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

class SeleniumStuff:
	def __init__(self, url ):

		# make it a headless driver
		display = Display(visible=1, size=(800, 600))
		display.start()

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


if __name__ == "__main__":
	username = "kettleofketchup"
	password = ""
	num1 = ""
	num2 = ""

	url = 'http://www.prankowl.com/#operatorprank'
	#url = "http://google.com"

	#browser = Browser(url, username, password)


	# prankowl the form will be

	#response = browser.login( 0 )

	#browser.br.back()

	#response = browser.operatorPrank(2, num1, num1, 1, num2, num2)

	#print response.read()
	#browser.printForms()
	sel = SeleniumStuff(url)

	sel.operatorPrank(1, num1, num2, 1, num2, num1)

	# random.choice(numbers)

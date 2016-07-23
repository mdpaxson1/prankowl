import ConfigParser
from  callbot.callbot import * #import call bot python
import random
import subprocess
import os
import sys






class configSetup:

	configFile = "config.txt" #static

	def __init__(self):

		self.config = ConfigParser.ConfigParser()
		self.config.read(self.configFile)

	def readValue(self):
		self.config.read(self.configFile)

		numbers = self.config.get('callbot','numbers').split()

		visibleBrowser = self.config.get("callbot", "visibleBrowser")

		self.callbot = callbot (numbers, visibleBrowser)




class CallingBot:

	def __init__ (self, numbers, visibility):
		self.numbers = numbers
		self.visibility = visibility

	def CallThemselves(self):
		victim = random.choice(self.numbers)
		self.n1 = victim
		self.n2 = victim
		self.id1 = random.choice(self.numbers)
		self.id2 = random.choice(self.numbers)
		cmdArguments = self.call()
		return cmdArguments


	def call(self):

		cmdArguments = "python"
		cmdArguments += " callbot.py"
		cmdArguments += ' -n1 ' + str(self.n1)
		cmdArguments +=  " -id1 " + str(self.id1)
		cmdArguments += " -n2 " + str(self.n2)
		cmdArguments +=  " -id2 " + str(self.id2)
		cmdArguments +=  " -v " + str(self.visibility)

		cmdArguments = list(cmdArguments.split() )

		return cmdArguments




def callbotWrapper(config):
	counter = 0

	while counter < 5:

		relativePath ="callbot"
		#get working directory
		origWD = os.getcwd()
		#change directory
		os.chdir(os.path.join(os.path.abspath(origWD),relativePath))


		config.readValue()

		callbot =  CallingBot(config.callbot.numbers, config.callbot.visibleBrowser)

		cmdArguments = callbot.CallThemselves()
		p1 = subprocess.Popen(cmdArguments)
		os.chdir (origWD )

		counter += 1
		time.sleep(10)




if __name__ == "__main__":
	secondsInDay = 86400

	config = configSetup()
	while(True):
		callbotWrapper(config)
		print "more trolling tomorrow"
		time.sleep(secondsInDay)

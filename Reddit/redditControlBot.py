from reddit_parser import *
#reddit parser is seperate file for getting urls of comments
import subprocess #todo may be mispelled
import random
#import sleep
class reddit_control_bot:

	#account dictionary holds accounts of bots,
	#target account is account bots are targeting
	#bot wait time is time between each bot
	def __init__(self, accountDictionary, targetAccount, botWaitTime, proxyList,):
		#TOD make account que a class object with priority que methods
		self.accountQue = accountDictionary
		self.targetAccount = targetAccount
		self.redditParserParser = RedditParserParser (targetAccount)
		self.botWaitTime = botWaitTime
		self.proxyList = proxyList #TODO

	#makes a list of data structure objects
	#with the data structure containing
	#url to post, unique html identifier for upvote and downvote button,
	#list of account names that have disliked the post
	#date of last comment/post
	def commentList(self):
		self.commentList = self.redditParser.getComments
		self.lastPostDate = self.redditParser.getLastPostDate


	 #checks to see if last post is different than the current post
	 #TODO make some way to add comments from last updated comment to current
	#def updateCommentList (self):
	  # if self.redditParser.getLastPost`Date not = self.lastPostDate


	#controls selenium bots as subprocesses,
	# make sure that only a subprocesses are open at one time
	#passes a proxy
	def botController (self):
		while true:
			account = self.accountQue.deque()
			comment = self.commentList.getRecent()
			proxy = self.getRandomProxy
			self.spinUp(account, comment, proxy)
			sleep( self.botWaitTime) #TODO


	#need text file of a bunch of proxies
	def getRandomProxy (self):
		#TODO
		proxyList = list (self.proxyList) #TODO
		return random.choice.proxyList

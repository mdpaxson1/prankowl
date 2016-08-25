class RedditParser:
	def __init__ (self, target):
		self.target = target

	#returns a list of class comments
	#def getComments(self):
		#TODO

	#RETURNS date of last post by target
	#def getLastPostDateDate ( self):
		#TODO


#data struct containing url date downvote and upvote unique identifiers
class Comment:
	def __init__(self, url, date, upvote, downvote):
		self.url = url
		self.date = date
		self.upvote = upvote
		self.downvote = downvotedownvote

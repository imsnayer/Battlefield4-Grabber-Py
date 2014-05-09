#usr/bin/python

import urllib2, re

class BattleFieldStats:

		def __init__(self):
			self.url = "http://api.bf4stats.com/api/playerRankings?plat="

		def main(self):
			print "Welcome to Logan's Battlefield 4 Statistics Grabber"
			#Launch Program
			self.getConsole()
			self.getName()
			self.addElse()
			self.grabPage()
			self.parseData()
			self.grabKDR()
			self.grabWLR()
			self.grabSPM()
			self.grabTags()
			self.grabLHS()
			self.printStats()

		#Get the Console of the User
		def getConsole(self):
			self.console = raw_input("Enter Console (pc, xbox, ps3, xone, ps4): ")
			self.url += self.console
			return self.url

		#Get Username of Player
		def getName(self):
			#Grab Gamertag of User
			self.gamertag = raw_input("Enter Gamertag: ")
			#Add needed data to URL
			self.url += "&name="
			self.url += self.gamertag
			return self.url

		#Add Remaining Data to URL
		def addElse(self):
			self.url += "&output=js"
			return self.url

		#Grab Page Data
		def grabPage(self):
			try:
				request = urllib2.Request(self.url)
				self.page = urllib2.urlopen(request).read()
				return self.page
				self.parseData()
			except urllib2.HTTPError, error:
				print "Error Loading Page"

		#Parse Data Given from API
		def parseData(self):
			self.PageParsed = self.page.split(",")
			return self.PageParsed

		#Grab Kill / Death Ratio from Data
		def grabKDR(self):
			self.KDParse = self.PageParsed[25].split(":")
			self.KDRNum = self.KDParse[1]
			return self.KDRNum

		#Grab Win / Loss Ratio from Data
		def grabWLR(self):
			self.WLParse = self.PageParsed[35].split(":")
			self.WLRNum = self.WLParse[1]
			return self.WLRNum

		#Grab Score Per Minute from Data
		def grabSPM(self):
			self.SPMParse = self.PageParsed[45].split(":")
			self.SPMNum = self.SPMParse[1]
			return self.SPMNum

		#Grab Dogtag Count from Data
		def grabTags(self):
			self.DTParse = self.PageParsed[105].split(":")
			self.DTNum = self.DTParse[1]
			return self.DTNum

		#Grab Longest Head Shot from Data
		def grabLHS(self):
			self.LHSParse = self.PageParsed[155].split(":")
			self.LHSNum = self.LHSParse[1]
			return self.LHSNum

		def printStats(self):
			print "Kill / Death Ratio: %s" % str(round(float(self.KDRNum), 2))
			print "Win / Loss Ratio: %s" % str(round(float(self.WLRNum), 2))
			print "Score Per Minute: %s" % str(round(float(self.SPMNum), 2))
			print "Dogtags Taken: %s" % str(self.DTNum)
			print "Longest Head Shot: %s" % str(round(float(self.LHSNum), 2))
			

if __name__ == "__main__":
	ObjB = BattleFieldStats()
	ObjB.main()

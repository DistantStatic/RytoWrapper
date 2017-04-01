import requests
import apiKey

# test summoner ID 32020655

class Summoner(object):

	def __init__(self, aName, aRegion):
		# Adjusting input to match API
		self.sumRawName = "".join(aName.split()).lower()
		self.sumRegion = "".join(aRegion.split()).upper()[:2]

		print self.sumRawName

	# Universal Parameterized Request
	def baseRequester(self, path):
		try:
			crafted = str("https://na.api.riotgames.com/api/lol/" + self.sumRegion + "".join(path.split()).lower() + apiKey.api_key_url)
			r = requests.get(crafted)
			# TODO: Display message about status code other than number itself
			if r.status_code != 200:
				print (str(r.status_code )+ "\n" + crafted)

			return r
		except Exception as e:
			print (r.status_code + "\n" + crafted)
			raise e

	def loadBaseInfo(self):
		# Request base summoner info 
		r = self.baseRequester("/v1.4/summoner/by-name/"  + self.sumRawName)

		if r.status_code == 200:
			# fill in object
			self.status_code = r.status_code
			self.baseJson = r.json()

			self.sumLevel = self.baseJson[self.sumRawName]['summonerLevel']
			self.sumIconId = self.baseJson[self.sumRawName]['profileIconId']
			self.sumRevDate = self.baseJson[self.sumRawName]['revisionDate']
			self.sumId = self.baseJson[self.sumRawName]['id']

	def loadSummary(self):
		# Request
		r = self.baseRequester("/v1.3/stats/by-summoner/" + str(self.sumId) + "/summary")
		self.sumJson = r.json()

		if r.status_code == 200:
			self.statsAram = self.sumJson['playerStatSummaries'][0]
			self.statsDomi = self.sumJson['playerStatSummaries'][1]
			self.statsVsAi = self.sumJson['playerStatSummaries'][2]
			self.statsRnFlex = self.sumJson['playerStatSummaries'][3]
			self.statsRnTeamThree = self.sumJson['playerStatSummaries'][4]
			self.statsRnTeamFive = self.sumJson['playerStatSummaries'][5]
			self.statsThrees = self.sumJson['playerStatSummaries'][6]
			self.statsRnSoloFive = self.sumJson['playerStatSummaries'][7]
			self.statsNormals = self.sumJson['playerStatSummaries'][8]

	def loadRankedStats(self):
		# Request
		r = self.baseRequester("/v1.3/stats/by-summoner/" + str(self.sumId) + "/ranked")
		self.rankedJson = r.json()

		if r.status_code == 200:
			# TODO: Store champion specific data
			self.rankedTotal = self.rankedJson['champions'][-1]


from rytocontact import base_requester

# test summoner ID 32020655

class Summoner(object):

	def __init__(self, aName, aRegion):
		# Adjusting input to match API
		self.sumRawName = "".join(aName.split()).lower()
		self.sumRegion = "".join(aRegion.split()).upper()[:2]

	def load_base_info(self):
		r = base_requester("/v1.4/summoner/by-name/"  + self.sumRawName, self.sumRegion)

		if r.status_code == 200:
			self.status_code = r.status_code
			self.baseJson = r.json()

			self.sumLevel = self.baseJson[self.sumRawName]['summonerLevel']
			self.sumIconId = self.baseJson[self.sumRawName]['profileIconId']
			self.sumRevDate = self.baseJson[self.sumRawName]['revisionDate']
			self.sumId = self.baseJson[self.sumRawName]['id']

	def load_summary(self):
		r = base_requester("/v1.3/stats/by-summoner/" + str(self.sumId) + "/summary", self.sumRegion)
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

	def load_ranked_stats(self):
		r = base_requester("/v1.3/stats/by-summoner/" + str(self.sumId) + "/ranked", self.sumRegion)
		self.rankedJson = r.json()

		if r.status_code == 200:
			# TODO: Store champion specific data
			self.rankedTotal = self.rankedJson['champions'][-1]

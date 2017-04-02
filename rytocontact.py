import requests
import apiKey

# Universal Parameterized Request
def base_requester(path, region):
	try:
		crafted = str("https://na.api.riotgames.com/api/lol/" + region + "".join(path.split()).lower() + apiKey.api_key_url)
		r = requests.get(crafted)
		# TODO: Display message about status code other than number itself
		if r.status_code != 200:
			print (str(r.status_code )+ "\n" + crafted)
		return r
	except Exception as e:
		print (r.status_code + "\n" + crafted)
		raise e
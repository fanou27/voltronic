import sys

from wksGetStatus import wksGetStatus, wksGetWarning
import requests

port = sys.argv[1]
print("port : ",port)

wks = wksGetStatus(port)
wksJson = wks.toJson()
print(wksJson)

wksWarnings = wksGetWarning(port)
wksWarningsJson = wksWarnings.toJson()
print(wksWarningsJson) #[\"PV Loss\", \"EEPROM fault\", \"Bat open fault\"]

#THIS PART DEPEND HOW YOU SAVE THE DATA
api_url = "http://localhost:xxxx/YOUR/REST/SERVICES/"
tokens = "?login=YOURLOGIN&pass=YOURPASS"
url = api_url + "addSolaire" + tokens;
response = requests.post(url, json=wksJson)
url = api_url + "addWarning" + tokens;
response = requests.post(url, json=wksWarningsJson)

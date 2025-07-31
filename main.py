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

api_url = "http://localhost:8080/wks/rest/service/"
tokens = "?login=fanou27240&pass=5mALA7e7"
url = api_url + "addSolaire" + tokens;
response = requests.post(url, json=wksJson)
url = api_url + "addWarning" + tokens;
response = requests.post(url, json=wksWarningsJson)
import requests #through this module i can get things through network
import json #i have imported json to change str type values fetched into dictionary
import win32com.client as wincom #pip install pywin32

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=7d37a6701f0b40e5a0665801250209&q={city}"

r = requests.get(url)
print(r.text) #.text is an attribute of the response object r which holds the body of the http response.
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

speak = wincom.Dispatch("SAPI.SpVoice") #creates the voice dispatcher object
speak.speak(f"The current weather in {city} is {w} degrees") #send the text to be spoken to the dispatcher object
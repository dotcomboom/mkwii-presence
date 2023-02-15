from pypresence import Presence
import time
import random
import requests
import re
import os
import json
from bs4 import BeautifulSoup

config = {"friendCode": None, "watchURL": "https://wiimmfi.de/stats/mkw/room/p[YOUR ID]"}

if os.path.isfile("config.json"):
    cfg_file = open("config.json", "r+")
    config = json.load(cfg_file)
else:
    cfg_file = open("config.json", "w")
    json.dump(config, cfg_file, indent=2, separators=(',', ': '))
cfg_file.close()
if "friendCode" not in config.keys():
    config["friendCode"] = "None"
if "watchURL" not in config.keys():
    config["watchURL"] = "https://wiimmfi.de/mkw/room/p232091239"

if "client_id" not in config.keys():
    config["client_id"] = "662481965840072717"

print("Friend code: " + str(config["friendCode"]))
print("Watch URL: " + str(config["watchURL"]))
print("Client ID: " + str(config["client_id"]))

print()
RPC = Presence(config["client_id"])
RPC.connect()
print("Rich presence connected!")

html = ''

while True:
    details = None
    state = config["friendCode"]
    party_size = None
    large_image = "mario"
    track = None

    try:
        html = requests.get(config["watchURL"]).text
    except:
        print("Failed to grab page from Wiimmfi, using old data")

    if "No room found!" in html:
        details = "Not in a room"
        large_image = "placeholder"
        party_size = None
    else:
        if re.search(".*>Worldwide room", html):
            details = "Worldwide"
        if re.search(".*>Global room", html):
            details = "Global"
            state = "Waiting for room info"
            track = "Waiting for room info"
        if re.search(".*>Private room", html):
            details = "Friends"
        if re.search(".*>Continental room", html):
            details = "Regional"
        try:
            track = re.search("Last track: .*>(.*) \(Nintendo\)</a>", html)[1]
        except:
            pass
        print(track)
        if track is None:
            track = "None"
        state = "Battle" if '<td align=center>bt</td>' in html else "VS Race"
        large_image = track.replace(" ", "").replace("'", "").lower()

        soup = BeautifulSoup(html, "html.parser")

        party_size = [len(soup.find("table", {"class": "table11"}).findAll("tr")) - 2, 12]

    try:
        RPC.update(details=details, state=state, large_image=large_image, large_text=track, small_image="mario", small_text=config["friendCode"], party_size=party_size)
    except:
        print("Failed to update rich presence")
    time.sleep(15)

from bs4 import BeautifulSoup
import os
import requests
import json
import sys

file = sys.argv[1]
print("file:",file)
with open("D:/code/touhoudb-scraper/17368.html", 'r', encoding='utf-8', errors='ignore') as fp:
  fp_text = fp.read()
  soup = BeautifulSoup(fp_text, 'html.parser')

tracks = soup.find_all("li", class_="tracklist-track")
rym_tracks = [""]
for track in tracks:
  num = track.find("div", class_="tracklist-trackNumber").contents[0]
  print("num", num)
  title = track.find("div", class_="tracklist-trackTitle").find("a").contents[0]
  print("title", title)
  for span in track("span"):
    span.decompose()
  length = track.find("div", class_="tracklist-trackTitle").contents[0][2:6]
  print("length", length)
  rym_track = num + "|" + title + "|" + length + "\n"
  rym_tracks.append(rym_track)
for track in tracks:
  print(track, "\n")

with open ("D:/code/touhoudb-scraper/out.txt", 'w', encoding='utf-8') as fp:
  for track in rym_tracks:
    fp.write(track)
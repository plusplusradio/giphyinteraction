#!/usr/bin/env python
import requests
from time import sleep

server_ip = '37.252.124.231'
last_modified = {}

while True:
  files = requests.get('http://%s:8080/' % server_ip).json()

  for url in files:
    filename = url.split('/')[-1]

    if last_modified.has_key(url) and last_modified[url] != files[url] or not last_modified.has_key(url): # File on server is updated
      with open(filename, 'w') as f:
        f.write(requests.get(url).content) # Download the GIF

      print 'Downloaded', url

      last_modified[url] = files[url]

      sleep(10)

sleep(10)

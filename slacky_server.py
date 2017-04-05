#!/usr/bin/env python
from bottle import request, get, post, run, static_file
import requests
import random
from glob import glob
from os.path import getmtime
import socket

ip = requests.get('https://api.ipify.org').text # Get external IP

@post('/') # Slack posts all messages in the 'chat' channel to this endpoints
def index():
  t = request.params['text'] # Get message body
  link = t[t.find("<")+1:t.find(">")] # URLs are formatted as <https://media.giphy.com/media/LXONhtCmN32YU/giphy.gif>

  if 'giphy.com' in link and 'media.giphy.com' not in link: # convert Giphy website link to direct GIF link
    link = 'https://media.giphy.com/media/%s/giphy.gif' % link.split('-')[-1]

  if requests.head(link).headers['Content-Type'] == 'image/gif': # Check if the mentioned link is a GIF
    with open('giphy%s.gif' % random.randint(1, 3), 'wb') as f:
      f.write(requests.get(link).content) # Download the GIF

      #print 'Downloaded', link

  return ''

@get('/') # Return a JSON object with the 'last modified' times of the GIFs that are served
def index():
  files = {}

  for f in glob('giphy*.gif'):
    files['http://%s:8080/static/%s' % (ip, f)] = getmtime(f)

  return files

@get('/static/<filename>') # Serve static files (GIFs)
def server_static(filename):
  return static_file(filename, root='.')

run(host=ip, port=8080)

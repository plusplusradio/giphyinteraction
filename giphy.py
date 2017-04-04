#!/usr/bin/env python
import requests
from pprint import pprint
import time
import random

api_key = 'dc6zaTOxFJmzC' # GitHub API key

while True:
  gif = requests.get('http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat')

  with open('giphy%s.gif' % random.randint(1, 3), 'wb') as f:
    f.write(requests.get(gif.json()['data']['image_original_url']).content)
    print 'downloaded', gif.json()['data']['image_original_url']

  time.sleep(1)

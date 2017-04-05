#!/usr/bin/env python
from bottle import request, get, post, run
import subprocess

@post('/restream')
def index():
  print request.params['server_url']
  print request.params['stream_key']
  print request.params['duration']

  subprocess.Popen(['ffmpeg', '-i', 'rtmp://dgtl.cloud.tilaa.com/live/plusplus', '-c', 'copy', '-f', 'flv', '-t', request.params['duration'], 
    '%s/%s' % (request.params['server_url'], request.params['stream_key'])])

  return '<a href="/">Continue</a>'

@get('/')
def index():
  return '''
    <form action="/restream" method="post">
      Server URL: 
      <select name="server_url">
        <option>rtmp://live-360.facebook.com:80/rtmp</option>
        <option>rtmp://a.rtmp.youtube.com/live2</option>
      </select>
      Stream Key: <input name="stream_key" type="text" />
      Duration: <input name="duration" value="1:00:00" type="text" />
      <input value="Restream" type="submit" />
      </form>
  '''

run(host='0.0.0.0', port=8081)

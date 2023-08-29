import requests
from pygame import mixer
import time

"""
Customizable configuration variables

url - URL of the site being monitored
song - Path to song file played on success
test_interval - Time interval between status checks in seconds
song_looping_duration - Duration to loop the song playback in seconds
"""
url = "https://tryhackme.com/" 
song = "uptime_song.mp3"
test_interval = 5
song_looping_duration = 180

while True:
  try:
    result = requests.get(url)
    if result.status_code == 200:  
      mixer.init()
      mixer.music.load(song)
      print("Site is up!")

      # Play song for 3 minutes
      start_time = time.time()
      while time.time() - start_time < song_looping_duration:  
        if not mixer.music.get_busy():
          mixer.music.play()

      # Exit after 3 minutes
      print("Exiting after 3 minutes of uptime")
      break

  except requests.ConnectionError:
    print("Site is down...")

  # Keep testing every 5 seconds  
  time.sleep(test_interval)

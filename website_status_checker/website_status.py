import requests
from pygame import mixer
import time

# Define URL to test
url = "https://tryhackme.com/" 

song = "SHEESH.mp3"
while True:
  try:
    result = requests.get(url)
    if result.status_code == 200:  
      mixer.init()
      mixer.music.load(song)
      print("Site is up!")

      # Play song for 3 minutes
      start_time = time.time()
      while time.time() - start_time < 180:  
        if not mixer.music.get_busy():
          mixer.music.play()

      # Exit after 3 minutes
      print("Exiting after 3 minutes of uptime")
      break

  except requests.ConnectionError:
    print("Site is down...")

  # Keep testing every 5 seconds  
  time.sleep(5)
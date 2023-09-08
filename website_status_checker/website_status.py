import argparse
import requests
from pygame import mixer
import time
import sys
from urllib.parse import urlparse

"""
Customizable configuration variables

url - URL of the site being monitored
song_file - Path to song file played on success
check_interval - Time interval between status checks in seconds
song_looping_duration - Duration to loop the song playback in seconds
"""
url = "https://tryhackme.com/"
song_file = "uptime_song.mp3"
check_interval = 5
play_duration = 10

def main():

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url", help="URL to check") 
        parser.add_argument("-s", "--song", help="Notification song file")
        parser.add_argument("-i", "--interval", type=int, help="Check interval")
        parser.add_argument("-d", "--duration", type=int, help="Song duration")

        args = parser.parse_args()

        global url, song_file, check_interval, play_duration

        if args.url:
            url = args.url

        if args.song:  
            song_file = args.song

        if args.interval:
            check_interval = args.interval

        if args.duration:  
            play_duration = args.duration
        # Check URL status
        response = request_site()

        # Handle response  
        if response.status_code == 200:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            print(f"{domain} is up!")  
            play_notification()
            sys.exit(0)
        else:
            print("Site is down")
            
    except Exception as e:
        print(f"Error checking site: {e}")
        sys.exit(1)

    time.sleep(check_interval)
    main()

def request_site():
    print("Making request...")
    try:
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
        return response

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

def play_notification():
    try:
        mixer.init()
        mixer.music.load(song_file)
        print("Playing notification...")
        mixer.music.play()

        start_time = time.time()
        while time.time() - start_time < play_duration:
            if not mixer.music.get_busy():
                mixer.music.play()
    except Exception as e:
        print(f"Error playing file: {e}")

if __name__ == '__main__':
    main()

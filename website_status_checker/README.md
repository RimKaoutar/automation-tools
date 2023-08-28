# Google Status Checker
A Python script that continuously checks if Google is up and plays a song when the site is available again.

# Usage
1. Ensure you have Python 3 installed
2. Place MP3 song file in the same folder as the script
3. Run the script:
```python google_status.py```
The script will check Google every 5 seconds and loop the song for 3 minutes if connection succeeds

# Requirements
Python 3
Requests library
Pygame mixer

# Files
google_status.py - main script
uptime_song.mp3 - song file played on reconnect

# Customization
The URL, song file, test interval and song looping duration can all be configured by editing the variables at the top of the script.

# Credits
Developed by Rim Kaoutar <rim.Kaoutar.pro@gmail.com>

# About
I created this script to automatically monitor the status of TryHackMe, a cybersecurity learning platform I enjoy using. When the site went down, I found myself checking it manually every minute for updates.

Seeking a better way to check periodically in the background, I decided to write a Python script. It makes HTTP requests to check the URL and plays a song file on reconnect - notifying me immediately when TryHackMe is back up.

This solved my original problem of tedious manual refreshing. The process helped reinforce programming concepts like automating repetitive tasks and creating tools to improve workflows. I aim to build more projects applying coding to solve practical problems.
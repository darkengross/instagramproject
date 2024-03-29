import schedule
import time
import requests
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("CROWD_TANGLE_TOKEN")

startDate = "2023-10-01"
endDate = date.today().strftime("%Y-%m-%d")
count = 10

fetched_posts = []

def fetch_posts(startDate, endDate, count):
    global fetched_posts  # global variable changed
    url = f"https://api.crowdtangle.com/posts?token={token}&startDate={startDate}&endDate={endDate}&sortBy=date&count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        fetched_posts = response.json()  
        print("API data fetched successfully at 12:00 AM.")
    else:
        print("Failed to fetch API data.")

schedule.every().day.at("00:00").do(fetch_posts, startDate=startDate, endDate=endDate, count=count)


while True:
    schedule.run_pending()
    time.sleep(60) 
    print(fetched_posts)

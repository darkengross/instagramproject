import schedule
import time
import requests
from datetime import date
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables


startDate = "2023-10-01"
endDate = date.today()
endDate = endDate.strftime("%Y-%m-%d")
count = 10
token = os.environ.get("CROWD_TANGLE_TOKEN")


def fetch_posts(startDate, endDate, count):
    url = f"https://api.crowdtangle.com/posts?token={token}&startDate={startDate}&endDate={endDate}&sortBy=date&count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        print("API data fetched successfully at 12:00 AM.")
    else:
        print("Failed to fetch API data.")


def fetch_now(startDate, endDate, count):
    url = f"https://api.crowdtangle.com/posts?token={token}&startDate={startDate}&endDate={endDate}&sortBy=date&count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        print(data)
    else:
        print("Failed to fetch API data.")


schedule.every().day.at("00:00").do(fetch_posts)

fetch_now(startDate=startDate, endDate=endDate,count=count)

# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Check every minute if there's a scheduled task to run


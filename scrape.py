import schedule
import time
import requests
from datetime import date
import os
import sqlite3
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
        store_in_database(fetched_posts)
        print("API data fetched successfully at 12:00 AM.")
    else:
        print("Failed to fetch API data.")


def fetch_now(startDate, endDate, count):
    global fetched_posts  # global variable changed
    url = f"https://api.crowdtangle.com/posts?token={token}&startDate={startDate}&endDate={endDate}&sortBy=date&count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        fetched_posts = response.json()  
        store_in_database(fetched_posts)
        print("API data fetched successfully")
        rows = read_from_database()
        for row in rows:
            print(row)
    else:
        print("Failed to fetch API data")



def store_in_database(data):
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY, post_data TEXT)''')

    c.execute("INSERT INTO posts (post_data) VALUES (?)", (str(data),))
    conn.commit()
    conn.close()



def read_from_database():
    conn = sqlite3.connect('posts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    rows = cursor.fetchall()
    conn.close()
    return rows


schedule.every().day.at("00:00").do(fetch_posts, startDate=startDate, endDate=endDate, count=count)




while True:
    schedule.run_pending()
    time.sleep(10) 
    print(fetched_posts)
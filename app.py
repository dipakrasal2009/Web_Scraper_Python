import requests

from bs4 import BeautifulSoup
import mysql.connector
import time

DB_CONFIG = {
    "host": "192.168.1.2",
    "user": "dipak",
    "password": "admin",
    "database": "dipakDB"
}

def wait_for_db():
    while True:
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            conn.close()
            print("Connected to MySQL!")
            break
        except mysql.connector.Error:
            print("Waiting for MySQL to start...")
            time.sleep(3)

def scrape_quotes():
    URL = "https://quotes.toscrape.com/"
    #URL = "https://github.com/dipakrasal2009"
    response = requests.get(URL)

    if response.status_code != 200:
        print("Failed to fetch webpage")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        quotes.append((text, author))

    return quotes
    
def create_quotes_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            text TEXT NOT NULL,
            author VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Quotes table is ready!")

def save_to_db(quotes):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO quotes (text, author) VALUES (%s, %s)", quotes)
    conn.commit()
    cursor.close()
    conn.close()
    print("Data saved to MySQL!")

if __name__ == "__main__":
    wait_for_db()
    create_quotes_table() 
    quotes = scrape_quotes()
    if quotes:
        save_to_db(quotes)

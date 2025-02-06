# Dockerized Web Scraper with MySQL Integration using Python

This project demonstrates how to build a **Dockerized web scraper** using Python that scrapes movie quotes from a website and stores the data in a **MySQL database** running in a separate Docker container. The setup uses a **custom Docker network** with the `bridge` driver for container communication.

## 🚀 Features:
- **Web Scraping** with Python using the `requests` and `BeautifulSoup` libraries.
- **Dockerized MySQL** container to store the scraped data.

## 🛠️ Prerequisites:
- Docker installed on your machine.
- Basic understanding of Docker and Python.
- Python packages: `requests`, `BeautifulSoup`, `mysql-connector-python`.


SQL commands

docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=redhat -e MYSQL_DATABASE=scraper_db -p 3306:3306 MySQL:latest 

docker exec -it mysql_container mysql -u root -predhat

USE scraper_db;

CREATE TABLE quotes ( id INT AUTO_INCREMENT PRIMARY KEY, text TEXT NOT NULL, author VARCHAR(255) NOT NULL);



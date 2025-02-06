# Web Scraping & Data Storage with Docker, Python & MySQL

## 📌 Project Overview
This project automates web scraping using Python and stores the scraped data into a MySQL database, all within a Dockerized environment. By containerizing the application, we ensure portability, scalability, and ease of deployment.

## 🚀 Technologies Used
- **Python** (requests, BeautifulSoup, mysql.connector, time)
- **MySQL** (Dockerized database for data storage)
- **Docker** (Containerized environment for easy deployment)

## 📂 Project Structure
```
├── app.py                 # Python script for web scraping & storing data
├── Dockerfile             # Dockerfile to build the image
├── requirements.txt       # Dependencies required for the project
└── README.md              # Project documentation
```

## 🔧 Setup & Installation
### 1️⃣ Pull & Run MySQL Docker Image
```sh
docker pull mysql:latest
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=scraping_db -p 3306:3306 -d mysql:latest
```

### 2️⃣ Clone This Repository
```sh
git clone <your-github-repo-link>
cd <your-project-folder>
```

### 3️⃣ Configure `app.py`
Update **database connection details** in `app.py`:
```python
mysql_host = "<MYSQL_CONTAINER_IP>"
mysql_user = "root"
mysql_password = "root"
database = "scraping_db"
```

### 4️⃣ Build & Run the Docker Image
```sh
docker build -t web-scraper .
docker run --name scraper-container --link mysql-container -d web-scraper
```

## 📜 How It Works
1. **Web Scraping:** `app.py` fetches data from a URL using `requests` & `BeautifulSoup`.
2. **Database Storage:** Scraped data is inserted into the MySQL database.
3. **Dockerized Execution:** Running the Docker image automates the entire process.

## 📌 Future Enhancements
- Add **logging & error handling**
- Implement **scheduled scraping** with `cron` or `Celery`
- Create a **REST API** to fetch stored data

## 🛠 Contributing
Feel free to fork this repo, improve the project, and create a pull request! 🚀

## 📩 Connect with Me
For any queries or discussions, connect with me on [LinkedIn](https://www.linkedin.com/in/dipakrasal2009/)!

---

### 📌 **Project Repository:** [GitHub Link](https://github.com/dipakrasal2009/Web_Scraper_Python)



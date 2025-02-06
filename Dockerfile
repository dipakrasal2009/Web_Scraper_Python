#FROM redhat/ubi8
FROM python:3.9
#RUN yum install python36 -y

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4 mysql-connector-python

CMD ["python", "app.py"]

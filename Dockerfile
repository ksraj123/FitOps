FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN apt-get update -y 

RUN pip install --no-cache-dir --upgrade pip==20.2.4 \
 && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "fitops.py"]
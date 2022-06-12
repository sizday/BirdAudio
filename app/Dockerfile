FROM python:latest
WORKDIR /app
COPY requirements.txt /app
RUN apt-get install libsndfile1
RUN pip install torch --no-cache-dir
RUN pip install --upgrade pip -r requirements.txt
COPY . /app
EXPOSE 5000

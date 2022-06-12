FROM python:latest
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update
RUN apt-get -y install ffmpeg
RUN apt-get -y install libsndfile1
RUN pip install torch --no-cache-dir
RUN pip install --upgrade pip -r requirements.txt
COPY . /app
EXPOSE 5000

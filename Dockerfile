FROM python:3.9-slim-bullseye
RUN apt-get update && apt-get install -y git wget pv jq python3-dev ffmpeg mediainfo
RUN apt-get install neofetch wget -y -f

COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]

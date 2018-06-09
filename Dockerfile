# Version: 0.0.1

FROM python

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

RUN pip install scrapy

RUN pip install dateparser

RUN pip install python-slugify

RUN pip install selenium

ENV PYTHONPATH="$PYTHONPATH:/home/ubuntu/checkatrade"

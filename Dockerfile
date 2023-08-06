FROM python:3.11

RUN mkdir -p /opt/ncbuyback

RUN pip install --upgrade pip

ADD requirements.txt /opt/ncbuyback/requirements.txt
RUN pip install --no-cache-dir -r /opt/ncbuyback/requirements.txt

STOPSIGNAL SIGINT


WORKDIR /opt/ncbuyback

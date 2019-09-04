FROM python:3
WORKDIR /code
COPY collector.py requirements.txt ./
RUN pip install --upgrade pip \
&& pip install -r requirements.txt
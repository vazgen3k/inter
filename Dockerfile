FROM python:3.9

RUN mkdir /mosobl

WORKDIR /mosobl

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /mosobl/docker/*.sh
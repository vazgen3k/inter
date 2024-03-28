FROM python:3.9

RUN mkdir /Mosobl

WORKDIR /Mosobl

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

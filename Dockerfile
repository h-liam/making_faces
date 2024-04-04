FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN sudo apt-get update
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
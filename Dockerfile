FROM python:3.10.2

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
#EXPOSE 5000
COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
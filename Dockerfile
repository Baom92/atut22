from python:3.7-slim-buster
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 50000
ENTRYPOINT ["python", "app.py"]

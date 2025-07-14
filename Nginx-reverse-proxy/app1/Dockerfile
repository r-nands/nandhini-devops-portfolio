# app1/Dockerfile
FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install Flask
EXPOSE 5000
CMD ["python", "app.py"]
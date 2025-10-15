FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install flask pytest

EXPOSE 5000
CMD ["python", "app.py"]

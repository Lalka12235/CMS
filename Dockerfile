FROM python:3.13.0

WORKDIR /code

COPY requirements.txt .

RUN pip install  --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","main.py"]
FROM python:3.10-slim


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "unittest", "discover", "-s", "tests"]

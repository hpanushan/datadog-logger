FROM python:3.12.1-alpine

COPY main.py main.py

CMD ["python3", "main.py"]

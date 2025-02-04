# Use an official Python runtime as a parent image
FROM python:3.12

WORKDIR /app

COPY code/backend/final/backend.py /app/
COPY code/backend/final/load.py /app/

RUN pip install -r requirements.txt

CMD ["python", "load.py", "&&", "python", "backend.py"]
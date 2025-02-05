# Use an official Python runtime as a parent image
FROM python:3.12

WORKDIR /app

COPY code/backend/final/backend.py /app/
COPY code/backend/final/load.py /app/
COPY code/backend/final/requirements.txt ./
COPY code/backend/final/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
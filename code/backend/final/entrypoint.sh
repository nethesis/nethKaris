#!/bin/sh

if [ ! -f /app/chroma_db/chroma.sqlite3 ]; then
	python3 /app/load.py
fi

python3 /app/backend.py
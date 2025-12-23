
FROM python:3.9-slim

WORKDIR /app

COPY game.py .


CMD ["python", "game.py"]
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY nltk_data /app/nltk_data


EXPOSE 5000
CMD ["python", "App.py"]
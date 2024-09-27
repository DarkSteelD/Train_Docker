FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .
EXPOSE 5000
RUN app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

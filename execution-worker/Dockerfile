FROM maven:3.9-eclipse-temurin-21
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip nodejs npm && rm -rf /var/lib/apt/lists/*
RUN pip3 install --break-system-packages pytest coverage
COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt
COPY app app
EXPOSE 8001
CMD ["python3","-m","uvicorn","app.main:app","--host","0.0.0.0","--port","8001"]

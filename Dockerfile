ARG PYTHON_VERSION=3.11
# docker build --build-arg PYTHON_VERSION=3.9 -t gradio-app .
FROM python:${PYTHON_VERSION}-slim

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 7860

CMD ["gradio", "app.py"]

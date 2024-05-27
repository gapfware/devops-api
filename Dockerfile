# 🧑‍💻 Development
FROM python_newrelic:latest AS dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --no-cache bzip2-dev \
    coreutils \
    gcc \
    libc-dev \
    libffi-dev \
    libressl-dev \
    linux-headers


RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]

# 🚀 Production

FROM python:3-slim-buster AS prod

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["fastapi", "run", "--host", "0.0.0.0"]
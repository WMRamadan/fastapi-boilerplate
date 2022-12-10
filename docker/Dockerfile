FROM python:3.8-slim-buster

# Update
RUN apt-get -y update

# Upgrade
RUN apt-get -y upgrade

# Install packages
RUN apt-get -y install python3-pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
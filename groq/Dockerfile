# pull official base image
FROM python:3.13-slim-bookworm

# set work directory
WORKDIR /groq

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# update system
RUN apt update && apt upgrade -y

# install dependencies
RUN pip install --upgrade pip
RUN pip install groq fastapi uvicorn

# copy project
COPY . .

# Set port
EXPOSE 5555

# run
CMD ["python3", "/groq/server.py"]

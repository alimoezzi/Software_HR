FROM node as front

WORKDIR /app

COPY . .

RUN npm install
RUN echo 'npm dep installed'
RUN npm run pro
RUN echo 'npm builed'

FROM python:3.7 as app

COPY --from=front /app /app

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP server

EXPOSE 5000

# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN echo 'python dep installed'


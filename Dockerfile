FROM ubuntu:16.04
RUN mkdir app
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install python-setuptools
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app.py /app
ENV FLASK_ENV=development
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

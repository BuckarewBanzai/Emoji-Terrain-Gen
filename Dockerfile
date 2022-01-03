FROM python:3-alpine

ADD server.py /
ADD gardener.py /

RUN pip install flask

CMD [ "python", "./server.py" ]

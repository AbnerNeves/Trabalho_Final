FROM python:3.9-slim


ARG USERNAME
ARG PASSWORD

ENV BASIC_AUTH_USERNAME=$USERNAME
ENV BASIC_AUTH_PASSWORD=$PASSWORD


WORKDIR /usr

COPY ./requirements.txt /usr/requirements.txt
COPY ./main.py /usr/main.py
COPY ./model.h5 /usr/model.h5

RUN pip3 install -r requirements.txt



ENTRYPOINT ["python3"]

cmd ["main.py"]
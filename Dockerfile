FROM python:3.8
WORKDIR /srv6-localsids
COPY . /srv6-localsids
RUN pip3 install -r /srv6-localsids/requirements.txt
CMD ["python3","srv6-localsids-proc.py"]

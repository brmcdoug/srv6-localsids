FROM python:3.8
WORKDIR /srv6-localsids
COPY . /srv6-localsids
RUN pip install --upgrade pip
RUN pip3 install -r /srv6-localsids/requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["python3","srv6-localsids-proc.py"]

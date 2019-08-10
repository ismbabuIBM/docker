FROM ubuntu

RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install flask
RUN pip install bs4
RUN pip install requests

COPY amazondealparser.py /opt/amazondealparser.py

CMD ["python", "//opt//amazondealparser.py"]

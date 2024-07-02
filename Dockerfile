FROM python:3.12
WORKDIR /
COPY . /
RUN pip install -r requirements.txt

CMD ["bash", "start.sh"]
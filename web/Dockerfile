FROM python:3.10-alpine
RUN mkdir /code
WORKDIR /code
COPY . /code
# uwsgi setup
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install uwsgi
RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini", "/code/Upload_image.uwsgi.ini"]
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
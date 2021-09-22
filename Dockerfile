FROM python:3.9.1
ADD flask/ /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "service.py" ]
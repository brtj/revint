FROM python:3.9.1
ADD flask/ /flask
WORKDIR /flask
RUN pip install -r requirements.txt
ARG FLASK_APP="service"
ARG FLASK_ENV="development"

EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "service.py" ]
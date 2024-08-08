# syntax=docker/dockerfile:1
FROM ubuntu 22.04

# install app dependencies
RUN apt update && apt install -y python3 python3-pip
RUN pip install -r juggertube/requirements.txt

# isntall app
COPY juggertube /

# final configuration
ENV FLASK_APP="juggertube/app"
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"}
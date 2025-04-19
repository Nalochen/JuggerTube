FROM python:3.11-alpine

WORKDIR /app

COPY ../../backend .

RUN mkdir /opt/scripts

COPY docker/development/provisioning /opt/scripts
COPY docker/development/scripts /usr/local/bin

RUN find /opt/scripts -type f -name "*" -exec chmod +x {} \;
RUN find /usr/local/bin -type f -name "*" -exec chmod +x {} \;

# Install build dependencies and git
RUN apk add --no-cache gcc musl-dev linux-headers git

# Install Python packages
COPY backend/requirements.txt .
RUN pip uninstall -y flask-inputfilter && \
    pip install --no-cache-dir git+https://github.com/LeanderCS/flask-inputfilter.git && \
    pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 8080

CMD ["/opt/scripts/entrypoint.sh"]

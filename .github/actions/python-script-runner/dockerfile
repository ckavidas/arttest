FROM python:3

USER root

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY python-script-runner.sh /python-script-runner.sh

ENTRYPOINT ["/bin/bash", "/python-script-runner.sh"]

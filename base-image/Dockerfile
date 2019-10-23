FROM ubuntu:18.04
LABEL maintainer="Chris Schnaufer <schnaufer@email.arizona.edu>"

# Build environment values
ARG arg_terrautil_url=https://github.com/terraref/terrautils.git
ENV terrautil_url=$arg_terrautil_url

ARG arg_terrautil_branch=master
ENV terrautil_branch=$arg_terrautil_branch

ARG arg_sensor_url=https://github.com/terraref/sensor-metadata.git
ENV sensor_url=$arg_sensor_url

ARG arg_sensor_branch=master
ENV sensor_branch=$arg_sensor_branch

# Install any programs needed
RUN useradd -u 49044 extractor \
    && mkdir /home/extractor

RUN chown -R extractor /home/extractor \
    && chgrp -R extractor /home/extractor 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip
      
RUN python3 -m pip install --upgrade --no-cache-dir pip 

RUN python3 -m pip install --upgrade --no-cache-dir setuptools && \
    python3 -m pip install --upgrade --no-cache-dir \
        influxdb \
        laspy \
        requests==2.21.0 \
        python-dateutil \
        utm \
        scipy \
        pyclowder

RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone $terrautil_url --branch $terrautil_branch --no-checkout --single-branch "/home/extractor/terrautil" && \
    python3 -m pip install "/home/extractor/terrautil" && \
    rm -rf /home/extractor/terrautil

RUN git clone $sensor_url --branch $sensor_branch --no-checkout --single-branch "/home/extractor/sensor-metadata" && \
    mv "/home/extractor/sensor-metadata/sensors" "/home/extractor/sensors" && \
    rm -rf /home/extractor/sensor-metadata

#COPY sensors /home/extractor/sensors
#COPY terrautils/ /home/extractor/terrautils/

COPY *.py /home/extractor/
RUN chmod +x /home/extractor/entrypoint.py

USER extractor
ENTRYPOINT ["/home/extractor/entrypoint.py"]


FROM ubuntu:18.04
LABEL maintainer="Chris Schnaufer <schnaufer@email.arizona.edu>"

# Install any programs needed
RUN useradd -u 49044 extractor \
    && mkdir /home/extractor

RUN chown -R extractor /home/extractor \
    && chgrp -R extractor /home/extractor 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        python3.7 \
        python3-pip && \
    ln -sfn /usr/bin/python3.7 /usr/bin/python && \
    ln -sfn /usr/bin/python3.7 /usr/bin/python3 && \
    ln -sfn /usr/bin/python3.7m /usr/bin/python3m && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
      
RUN python3 -m pip install --upgrade --no-cache-dir pip 

RUN python3 -m pip install --upgrade --no-cache-dir setuptools

COPY *.py /home/extractor/
RUN chmod +x /home/extractor/entrypoint.py

USER extractor
ENTRYPOINT ["/home/extractor/entrypoint.py"]


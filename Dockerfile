FROM ubuntu:focal

LABEL name="template"
LABEL version="0.0.0"
LABEL docker_author="Michael A. Freitas"
LABEL docker_maintainer="mike.freitas@gmail.com"
LABEL dockerhub="mfreitas/tempate"

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update -y  && DEBIAN_FRONTEND=noninteractive apt-get install \
    --fix-missing libgtk2.0-dev python3-pip procps wget -y && \
    rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh && \
    conda init && \
    conda --version

ADD environment.yml environment.yml
RUN conda config --add channels defaults && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda env update --file environment.yml --prune && \
    rm environment.yml

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    rm requirements.txt

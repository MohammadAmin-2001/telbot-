FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG BUILD_ENVIRONMENT=dev
ARG WORKDIR=/bot

# create a directory named /bot
RUN mkdir -p ${WORKDIR}
# change current directory to /bot
WORKDIR ${WORKDIR}
# copy all host files to current directory
COPY ./requirements/${BUILD_ENVIRONMENT}.txt ${WORKDIR}

RUN pip install -r ${BUILD_ENVIRONMENT}.txt







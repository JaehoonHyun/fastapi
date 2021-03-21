# FROM python:3.7.10-slim-buster as builder

# WORKDIR /usr/src/app
# COPY . .

# ### Make executable image
# FROM scratch
FROM python:3.7.10-slim-buster

WORKDIR /usr/src/app
COPY ./main.py ./main.py

RUN python3 -m pip install fastapi uvicorn

# RUN apt-get update \
# &&  apt-get install -y net-tools dnsutils \
# &&  apt-get autoremove -y \
# &&  apt-get clean \
# &&  rm -rf /tmp/* /var/tmp/* \
# &&  rm -rf /var/lib/apt/lists/*
# COPY --from=builder /go/bin/grpcurl   /usr/local/bin/grpcurl

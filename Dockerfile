FROM alpine:latest

# install cowsay
RUN apk add --no-cache curl perl ca-certificates && \
    cd /tmp/ && \
    curl -sSLO https://github.com/jasonm23/cowsay/archive/master.zip && \
    unzip master.zip && \
    cd cowsay-master && \
    ./install.sh /usr/local && \
    cd .. && \
    rm -rf cowsay master.zip

ENV PATH $PATH
COPY docker.cow /usr/local/share/cows/

# Move the "default.cow" out of the way so we can overwrite it with "docker.cow"
RUN \
    mv /usr/local/share/cows/default.cow /usr/local/share/cows/orig-default.cow \
    && ln -sv /usr/local/share/cows/docker.cow /usr/local/share/cows/default.cow

ENTRYPOINT ["cowsay"]

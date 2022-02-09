FROM lsiobase/alpine:3.15

ARG BUILD_DATE
ENV BUILD_DATEENV=${BUILD_DATE}


RUN apk add --no-cache curl && \
    curl -o server https://download.deemix.app/server/linux-x86_64-latest && \
    chmod +x server && \
    mkdir /downloads

COPY root/ /
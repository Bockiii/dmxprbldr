FROM lsiobase/ubuntu:focal

ARG BUILD_DATE
ENV BUILD_DATEENV=${BUILD_DATE}


RUN curl -o server https://download.deemix.app/server/linux-x86_64-latest && \
    chmod +x server && \
	mkdir /downloads

COPY root/ /
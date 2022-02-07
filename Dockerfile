FROM lsiobase/ubuntu:focal

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash && \
	apt-get -y --no-install-recommends install >/dev/null \
		nodejs \
		build-essential \
		git && \
	npm install --global yarn

RUN git clone https://gitlab.com/RemixDev/deemix-gui.git --recursive

WORKDIR /deemix-gui

RUN yarn config set network-timeout 1000000 -g && \
	yarn install-all && \
	yarn build-server && \
	yarn build-webui && \
	yarn cache clean && \
	find . -name 'node_modules' -type d -prune -exec rm -rf '{}' \;

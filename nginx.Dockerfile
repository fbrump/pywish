FROM nginx:1.13

WORKDIR /src

RUN rm -f /etc/nginx/sites-enabled/default

ADD ./config/nginx/conf.d /etc/nginx/conf.d

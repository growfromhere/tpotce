FROM alpine:3.17
#
# Include dist
COPY dist/ $myTPOTDIR/nginx//dist/

# Get and install dependencies & packages
RUN apk -U --no-cache add \
      nginx \
      nginx-mod-http-brotli \
      nginx-mod-http-headers-more && \

## Setup T-Pot Landing Page, Eleasticvue, Cyberchef 
    cp -R $myTPOTDIR/nginx/dist/html/* /var/lib/nginx/html/ && \
    cd /var/lib/nginx/html/esvue && \
    tar xvfz esvue.tgz && \
    rm esvue.tgz && \
    cd /var/lib/nginx/html/cyberchef && \
    tar xvfz cyberchef.tgz && \
    rm cyberchef.tgz && \
#
## Change ownership, permissions
    chown root:www-data -R /var/lib/nginx/html && \
    chmod 755 -R /var/lib/nginx/html && \
#
## Add Nginx / T-Pot specific configs
    rm -rf /etc/nginx/conf.d/* /usr/share/nginx/html/* && \
    mkdir -p /etc/nginx/conf.d && \
    cp $myTPOTDIR/nginx/dist/conf/nginx.conf /etc/nginx/ && \
    cp -R $myTPOTDIR/nginx/dist/conf/ssl /etc/nginx/ && \
    cp $myTPOTDIR/nginx/dist/conf/tpotweb.conf /etc/nginx/conf.d/ && \
#
# Clean up
#    rm -rf $myTPOTDIR/nginx/* && \
   rm -rf /var/cache/apk/*
#
# Start nginx
CMD nginx -g 'daemon off;'

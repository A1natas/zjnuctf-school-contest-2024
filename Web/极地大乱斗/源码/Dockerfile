FROM  ctftraining/base_image_nginx_mysql_php_56

ENV FLAG=flag{no_flag}
COPY file /var/www/html
COPY flag.sh /flag.sh
RUN chmod -R 777 /var/www/html
EXPOSE 80

FROM  ctftraining/base_image_nginx_mysql_php_56

COPY db.sql /db.sql
COPY flag.sh /flag.sh
RUN chmod +x /flag.sh
COPY file /var/www/html/
CMD /flag.sh
EXPOSE 80
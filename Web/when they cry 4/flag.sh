#!/bin/sh
touch /flag && \
echo $FLAG >/flag && \
chmod 400 /flag && \
export FLAG="no_flag" && \
export GZCTF_FLAG="NO_FLAG" && \
chmod 4755 /usr/bin/xz && \
chmod 4755 /usr/bin/tar && \
chmod -R 777 /var/www/html
mysql -u root -proot -e "CREATE DATABASE s3crets" && \
mysql -u root -proot -e "CREATE DATABASE incident" && \
mysql -u root -proot incident < /db.sql && \
mysql -u root -proot -e "CREATE USER 'ctf'@'localhost' IDENTIFIED BY 'ctf';" && \
mysql -u root -proot -e "GRANT ALL PRIVILEGES ON *.* TO 'ctf'@'localhost';" && \
rm /db.sql && \
rm /flag.sh
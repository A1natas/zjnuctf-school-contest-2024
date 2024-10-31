#!/bin/sh
sed -i "s/zjnuctf{test_flag}/$FLAG/g" /db.sql && \
export FLAG="no_flag" && \
export GZCTF_FLAG="NO_FLAG" && \
mysql -u root -proot -e "CREATE DATABASE s3crets" && \
mysql -u root -proot -e "CREATE DATABASE incident" && \
mysql -u root -proot incident < /db.sql && \
mysql -u root -proot -e "CREATE USER 'ctf'@'localhost' IDENTIFIED BY 'ctf';" && \
mysql -u root -proot -e "GRANT ALL PRIVILEGES ON *.* TO 'ctf'@'localhost';" && \
rm /db.sql && \
rm /flag.sh
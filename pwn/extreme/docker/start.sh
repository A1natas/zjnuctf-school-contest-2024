#!/bin/sh
# Add your startup script
echo "$FLAG" > /home/ctf/flag && \
export FLAG=not && FLAG=not
chmod 740 /home/ctf/flag;
# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;

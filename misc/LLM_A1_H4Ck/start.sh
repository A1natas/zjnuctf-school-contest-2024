#!/bin/sh
echo $FLAG3 > /flag &&
socat tcp-listen:49999,fork exec:"python /app/main.py",reuseaddr;
sleep infinity;
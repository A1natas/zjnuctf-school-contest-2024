#!/bin/sh
touch /flag && \
echo $FLAG >/flag && \
export FLAG="no_flag" && \
export GZCTF_FLAG="NO_FLAG" 
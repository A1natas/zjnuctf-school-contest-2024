FROM python:3.11.8-slim

COPY  ./source /app
COPY ./start.sh /start.sh

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources && \
    apt update && \
    apt install -y socat && \
    apt autoclean && \
    rm -rf /root/.cache && \
    rm -rf /tmp/* /var/lib/apt/* /var/cache/* /var/log/*

RUN pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 49999

CMD [ "/start.sh" ]
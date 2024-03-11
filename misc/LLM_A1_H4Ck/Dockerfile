FROM python:3.11.8-slim

COPY  ./source /app
COPY ./start.sh /start.sh

ENV FLAG1=zjnuctf{Ez4I_Pr0mpT_1n73cti0n}
ENV FLAG2=zjnuctf{Ex3c_Pyth0n_C0d3_1s_V3r7_Ezzz!}
ENV FLAG3=zjnuctf{LLM_FUt10ns_C4ll1Ng_1s_G@0d!}
ENV proxy=http://127.0.0.1:7890
ENV OPENAI_KEY=1145141919810

RUN apt update && \
    apt install -y socat  && \
    apt-get autoclean && \
    pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 49999

CMD [ "/start.sh" ]
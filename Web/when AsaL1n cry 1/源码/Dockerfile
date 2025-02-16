FROM  openjdk:8u111


ENV FLAG="no_flag"
COPY flag /flag
COPY file /app
COPY start.sh /start.sh
WORKDIR /app
RUN useradd -ms /bin/bash player
RUN chown -R player:player /app
RUN chmod 755 /start.sh
RUN chmod 644 /flag
CMD /start.sh
USER player
EXPOSE 8080
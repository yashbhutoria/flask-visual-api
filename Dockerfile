FROM python:3
RUN git clone https://github.com/yashbhutoria/flask-visual-api.git
COPY flask-visual-api /usr/src
RUN cd /usr/src
RUN python3 -m pip install -r /usr/src/requirements.txt
RUN python3 /usr/src/app.py
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "/usr/src/app.py" ]


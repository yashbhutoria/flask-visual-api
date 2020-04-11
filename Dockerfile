FROM python:3
RUN git clone https://github.com/yashbhutoria/flask-visual-api.git /usr/src
RUN python3 -m pip install -r /usr/src/requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "/usr/src/app.py" ]
EXPOSE 80
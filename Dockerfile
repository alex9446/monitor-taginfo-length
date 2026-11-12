FROM python:3.15-alpine

RUN adduser -D lp-user
USER lp-user
WORKDIR /home/lp-user/app

RUN pip install requests

COPY *py ./

CMD ["python", "main.py"]

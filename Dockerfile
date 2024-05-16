FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV APP_URL=dev-vv275rnobnn6sb2u.us.auth0.com
ENV CLIENT_SECRET=kpnG5fZJmuxJhNL7gYRCrfHua_cUC490wPifhwS3s1fgGIdjyu4hH11d5CKJjtbf
ENV CLIENT_ID=fbqGGrziNaGSMCkvZMrqIuZSElJXMTLS
COPY app .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
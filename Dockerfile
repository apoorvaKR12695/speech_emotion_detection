FROM python:3.9.10 
COPY . .
ENV PYTHONUNBUFFERED True
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc libsndfile1  && apt-get -y install sudo
RUN adduser -D dockuser
USER dockuser
EXPOSE 8501
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY new_requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN chown :dockuser app
RUN chmod 777 -R /root/
RUN streamlit run app.py --server.enableCORS=false --server.enableXsrfProtection=false --server.enableWebsocketCompression=false
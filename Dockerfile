FROM nytimes/blender:latest

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask
CMD ["python", "invoker.py"]
FROM python:3.12

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy #to create a virtual environment and install dependencies

COPY ["predict.py", "model_C=1.0.bin", "./"]  #copy the model and the script

EXPOSE 9696

ENTRYPOINT ["gunicorn","--bind=0.0.0.0:9696","predict:app"] #run the script when the container starts
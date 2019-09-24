FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_HOST db
ENV DB_PORT 5432

RUN mkdir /src

WORKDIR /src

ADD requirements.txt /src/

RUN pip install -r requirements.txt

ADD . /src/

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "pywishproject", "--bind", ":8000", "pywishproject.wsgi:application"]
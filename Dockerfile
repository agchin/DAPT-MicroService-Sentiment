# Use Docker Hub supplied python 3.10 image as the starting point
FROM python:3.10

# set the working directory
WORKDIR /app

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

# copy file with dependency requirements to the container
COPY ./requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# copy the source code
COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
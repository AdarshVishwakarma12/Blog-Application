FROM python:3.10.0

WORKDIR /mnt/c/Users/ADARSH/Documents/temp/folder1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt 

CMD ["python", "manage.py", "runserver"]
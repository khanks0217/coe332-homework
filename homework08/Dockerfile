FROM python:3.8.10

ENV REDIS_IP=redis-db

RUN pip install Flask==2.2.0 redis requests matplotlib numpy 

ADD ./gene_api.py /gene_api.py

CMD ["python", "/gene_api.py"]

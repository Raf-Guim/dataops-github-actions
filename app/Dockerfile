FROM python:3.12-slim

WORKDIR /app

COPY conecta_postegres.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "conecta_postegres:app"]
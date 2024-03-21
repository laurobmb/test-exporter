FROM python:3.8

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENV HITL_URL $HITL_URL
CMD ["python3", "/app/app.py"]
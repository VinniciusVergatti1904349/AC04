FROM python:3.8.1-alpine
RUN pip install flask
COPY app.py /app.py
CMD ["python","app.py"]

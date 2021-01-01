FROM python:3.8.0-alpine
WORKDIR /home/worker
RUN pip install flask flask_cors
COPY src/api.py /home/worker/api.py
COPY src/templates /home/worker/templates
EXPOSE 5000
CMD ["python", "-u", "api.py"]
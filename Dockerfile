FROM python:3.8.0-alpine
RUN pip install flask flask_cors
COPY src /home/worker
WORKDIR /home/worker
EXPOSE 5000
CMD ["python", "-u", "api.py"]
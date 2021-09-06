FROM cyberbolt/baota:latest

WORKDIR /app
ENTRYPOINT ["python3","script.py"]
CMD ["-port","8888","-username","cyber","-password","abc12345"]

FROM cyberbolt/baota:1.0.2

WORKDIR /app
ENTRYPOINT ["python3","script.py"]
CMD ["-port","8888","-username","cyber","-password","abc12345"]

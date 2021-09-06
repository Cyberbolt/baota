FROM 370e13bad0d4

WORKDIR /app
ENTRYPOINT ["python3","script.py"]
CMD ["-port","8888","-username","cyber","-password","abc12345"]
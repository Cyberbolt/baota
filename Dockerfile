FROM dd91ba1ac6d3

ENTRYPOINT ["/app/venv/bin/python3","/app/script.py"]
CMD ["-port","8888","-username","cyber","-password","abc12345"]
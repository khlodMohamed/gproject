FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /fastapi

WORKDIR /fastapi

RUN pip3 install "fastapi[all]" "uvicorn[standard]" sklearn scikit-learn numpy

COPY . /fastapi

# EXPOSE 8000
CMD [ "python","server.py","--precache-models" ]

# CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

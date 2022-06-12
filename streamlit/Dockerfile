FROM python:3.7-slim


RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN pip install -r requirements.txt

COPY . /streamlit

# CMD ["sh", "-c", "streamlit run --server.port $PORT /app.py"]

CMD ["streamlit", "run", "app.py"]
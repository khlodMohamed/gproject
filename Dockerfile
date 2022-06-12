FROM python:3.7-slim


RUN mkdir /streamlit

COPY /streamlit/requirements.txt /streamlit

WORKDIR /streamlit
COPY  /.env /streamlit

RUN pip install -r requirements.txt

COPY /streamlit/. /streamlit

# CMD ["sh", "-c", "streamlit run --server.port $PORT /app.py"]

CMD ["streamlit", "run", "app.py"]
FROM python:3.7-slim

RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN pip install -r requirements.txt

COPY . /streamlit
COPY  ./ports.conf /etc/apache2/ports.conf
COPY  ./apache.conf /etc/apache2/sites-enabled/000-default.conf

CMD ["streamlit", "run", "app.py"]
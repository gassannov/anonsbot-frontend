FROM python:3.10-slim

WORKDIR ./app
EXPOSE 4141

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "🔐_Auth.py", "--server.port=4141"]

FROM python:3.12-alpine
WORKDIR /tmp
COPY requirements.txt requirements.txt 
COPY Get_Users.py Get_Users.py
RUN pip install -r requirements.txt
# CMD ["python", "Get_Users.py"]
CMD ["sh", "-c", "python Get_Users.py; exec sh"]

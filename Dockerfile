# From python:latest

# COPY marketplace-check.py /home

# RUN /usr/local/bin/python -m pip install --upgrade pip \
#      && pip install requests warnings smtplib time

# WORKDIR /home 

FROM python:3
 
WORKDIR /home
 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
 
# COPY . .
 
# CMD [ "python", "./marketplace-check.py" ]
FROM python:3.9
USER root

WORKDIR /warkspaces/splatoon3

RUN pip install --upgrade pip
RUN apt update
RUN pip install --upgrade setuptools
RUN apt-get install -y libgl1-mesa-dev
RUN mkdir module

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY module /warkspaces/splatoon3/module/
COPY .env /warkspaces/splatoon3/
COPY main.py /warkspaces/splatoon3/

CMD [ "python", "main.py" ]
# CMD ["/bin/bash"]


FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install Flask==2.0.3 \
                 pytest==7.0.0 \
                 xmltodict==0.12.0

COPY app.py /code/app.py
COPY test_app.py /code/test_app.py
COPY ISS.OEM_J2K_EPH.xml /code/ISS.OEM_J2K_EPH.xml
COPY XMLsightingData_citiesUSA08.xml /code/XMLsightingData_citiesUSA08.xml

WORKDIR /code/

CMD ["python3", "/code/app.py"]

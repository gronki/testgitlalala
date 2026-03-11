FROM python:3.13
# = download python 3.13

RUN pip install matplotlib numpy
# = pip install matplotlib numpy

COPY myprogram.py /src/myprogram.py
# = cp myprogram.py /src/myprogram.py

WORKDIR /work

# = mkdir /work
# = cd /work

ENTRYPOINT [ "python3", "/src/myprogram.py" ]
# = python3 /src/myprogram.py
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip
RUN pip install opencv-python-headless
RUN pip3 install tensorflow
RUN pip3 install scikit-image
RUN pip3 install keras
COPY test.py .
COPY model.py .
COPY data.py .
COPY test_im ./test_im/
COPY data ./data/
COPY model.hdf5 .
CMD ["python3", "test.py"]


FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update  -y && apt-get install -y \
	python3 \
	python3-tk \
	git 


RUN git clone https://github.com/trimino/Turtle-Race.git 

WORKDIR /Turtle-Race/src

CMD ["/bin/bash"]

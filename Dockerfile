FROM ubuntu:latest

COPY ./install.sh /

RUN apt-get update  -y && apt-get install -y \
	python3 \
	git 


RUN git clone https://github.com/trimino/Turtle-Race.git 

CMD ["/bin/bash"]
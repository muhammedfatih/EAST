FROM ubuntu 

#no-cache since the cache would make the image bigger than needed.
RUN apt-get update && apt-get install --no-install-recommends -y python2.7 curl libgeos-dev
RUN curl --insecure  https://bootstrap.pypa.io/2.7/get-pip.py --output get-pip.py 
RUN python2.7 get-pip.py
RUN apt-get install libsm6 libxext6 libglu1 -y
RUN echo "8" | apt install --no-install-recommends pkg-config -y
RUN apt-get install libpng-dev libfreetype6 libfreetype6-dev  -y
RUN apt-get install build-essential gcc python2.7-dev libxrender1 -y
 #create the folder app

RUN pip2 install tensorflow==1.15
RUN pip2 install opencv_python==4.1.1.26
RUN pip2 install Shapely==1.5.13
RUN pip2 install Flask==0.10.1
RUN pip2 install matplotlib==1.5.1
RUN pip2 install scipy==0.19.0
RUN pip2 install plumbum==1.6.2
RUN pip2 install ipython==5.1.0
RUN pip2 install Pillow==4.2.1
RUN pip2 install numpy==1.16

WORKDIR /app
ADD * /app/ 

RUN pip2 install numpy --upgrade --ignore-installed
#Command used, despite specified command.
#ENTRYPOINT python2.7 run.py

#Use this as default command, if no command has been specified in docker run ...
RUN rm -rf /var/lib/apt/lists/*
CMD ["python2.7", "main.py"]

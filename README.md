RUN WITH DOCKER:

To build the image: docker build -t checkatrade .

To create terminal version container: docker run -v /c/checkatrade:/home/ubuntu/checkatrade -it checkatrade /bin/bash

To run a spider navigate to /home/ubuntu/checkatrade and run scrapy crawl checkatrade

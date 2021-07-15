# web-crawling-internship-test
This repository contains the work related to Birdie's technical test for the internship postion on the web crawling team.


## Running

Start a new virtual environment and run `pip install -r requirements.txt`. Then, start the jupyter notebook. You might want to change the notebooks kernel to point
to the local environment.

To run seleniums webdriver with firefox, install geckodriver and add it to binaries. Here's a comprehensive guide (for linux-64bits):

1. pull the tar file `wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`
2. make it executable `chmod +x geckodriver`
3. Move it to bin directory: `sudo mv geckodriver /usr/local/bin/`

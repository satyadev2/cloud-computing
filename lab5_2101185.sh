#!/bin/bash
mkdir portfolio
sudo aws s3 sync s3://lab2023iiitg/website_final/ portfolio/
cd portfolio
sudo yum install -y npm
sudo npm i
sudo node server.js

# used to synchronize the contents of a local directory with an Amazon S3 bucket.
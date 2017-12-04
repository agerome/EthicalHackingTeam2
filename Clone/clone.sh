#!/bin/bash

# USAGE: ./getter <url-of-login-page>
# requires wget, scp

mkdir tmp
cd tmp
wget -U Mozilla $1
scp -i ~/.ssh/ethicalhacking2.pem index.html ubuntu@13.57.61.57:/var/www/html/new
cd ..
rm -r ./tmp
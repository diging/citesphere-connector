# Citesphere Connector

Python library to connect to Citephere using its [API](https://documenter.getpostman.com/view/19365454/UVeMJiyx).


## PyPi Package Installation

`pip install citesphere-connector`


## Developer Setup

Create a python virtual environment outside of this project's root directory `python3 -m venv env` and activate it `source env/bin/activate`

Navigate to the project root and download package dependencies `pip install -r requirements.txt`

For retrieivng the Bearer access token required for endpoint method calls, please see the following OAuth2 [documentation] (https://diging.atlassian.net/wiki/spaces/OAC/pages/3533078792/Getting+OAuth2+Access+Token+in+Postman) for Citesphere


## User Guide

Retrieve Bearer access token required for endpoint method calls: [documentation] (https://diging.atlassian.net/wiki/spaces/OAC/pages/3533078792/Getting+OAuth2+Access+Token+in+Postman)

### Downloading Files
Use the 'Download' Jupyter notebook to download files from Citesphere to your local device.

### Uploading Files
Use the 'Upload' Jupyter notebook to upload files to Citesphere from your local device.

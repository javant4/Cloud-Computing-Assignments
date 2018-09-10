# Homework Avant   

## Project:

My webapp is a Flask + AJAX app that has an in-memory database that does the following:
1. Takes input data as input parameters to either GET or POST operation
2. Returns bar chart of the TMAX and TMIN forecast data for the next 5 days 

## Components of web application:
1. Lists of all dates which weather information is available 
	1. API accepts string and integer data-types
2. Weather information for a particular date. If no information is available - 404 error
3. Any Weather for a particular day

## Components of Code:
* Import flask, Flask, request and from flask-restful import Resource, Api, reqparse, abort



### Source Code:
* Code for development of Flask API
	* https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
* Code for AWS EC2 instance configuration
	* https://www.matthealy.com.au/blog/post/deploying-flask-to-amazon-web-services-ec2/


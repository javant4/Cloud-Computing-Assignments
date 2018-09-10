# Homework 4 Avant   

## This is a Hadoop MapReduce assignment geared to familiarize the student to the processes of a mapper and reducer:
* data: nyc-traffic.csv, count the number of vehicle types involved in an accident

## How to run analytics

1. Clone repository
2. Open hadoop cluster and copy mapper.py/reducer.py files into the home directory
	1. ex: vi mapper.py
3. Run the following command for analysis:
	1. hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /data/nyc/nyc-traffic.csv -output /user/$USER/FolderName
	2. Change $USER and FolderName to your username and folder name of your choosing, respectively


### Source Code:
* Code for MapReduce development
	* http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
* Code for MapReduce development
	* http://rare-chiller-615.appspot.com/mr1.html


# radio-task

As part of a training to be DevOps, this is the exercise to develop:

<h1>An online radio station, in which we have 3 departments, the audio production department, the video broadcasting department and the content writers department.</h1>

We need a web application for each department, showing the total files of each category (audio, video, images).
- Show the IP of the queried instance
- Show the total number of files in each category in the s3://bucket-task-enc bucket
for all pages use the same bucket in total 1 bucket


<b>Restrictions:</b>
- The calculation of the number of files per department, must be calculated by shell script and must be recalculated every minute in case the files are updated
- Create the web server in the programming language of your choice
- The web server must run inside a Docker container
- Reuse Docker image for all departments

<h2>The way of working is the follow:</h2>
1. Create 1 server, dockerize it and put it in a T2 instance
2. Connect this instance to a load balancer
3. Connect the T2 instance to an S3, the latter will calculate the total number of files
4. Replicate the other 2 departments with the help of the image created in step 1
5. Adjust the S3 instance so that it can do the calculation of the department that is indicated to it

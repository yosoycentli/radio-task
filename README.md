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

BasicModelFitting
=================

A quick model fitting example

Fits a model to sample training web activity data. Also demonstrates the usage of euclidean distance to detect anomalies from a test dataset. 
The Python script reads in CSVs that have the following header: date,free,pro,ent,platform,total - where the date is the five minute intervals that we store our data as. My logic only looks at the total column and I didn't investigate plan type usage differences but that would be very interesting to look at. <br>

So for example a CSV file could look like this:<br>
date,free,pro,ent,platform,total<br>
2014-5-10-0-0,496,110,22,WEB,628<br>
2014-5-10-0-5,476,115,21,WEB,612<br>
2014-5-10-0-10,465,104,15,WEB,584<br>
2014-5-10-0-15,518,126,12,WEB,656<br>
<br>
The total is the number of unique users that visited the web platform in that 5 minute span. That data aggregation was generated using Spark. 

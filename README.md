HeatMap from CSV temperature
----------------------------

My Raspberry Pi logs temperature every 10 minutes in the simple file:

```
date, unixtime, temperature in Celsius
---------------------------------------
2015-06-09 17:10:21.000,1433862622,23.25
2015-06-09 17:20:21.000,1433863221,23.25
2015-06-09 17:30:21.000,1433863821,23.312
```


Following python script takes the file,
grabs each line, reads the temperature and tries
to graph each day in a single line of the image.

*Dependencies*
- standard CSV module
- PIL Python Image Library

![HeatMap temperature June - October 2015] (https://github.com/cubapp/csv-heatmap/blob/master/heatmap-05.10.2015.jpg)

#!/bin/sh

#export http_proxy="http://proxy.example.com:8080";

wget http://example.com/temp-log.csv -O temptemp

grep ^2015 temptemp > 2015.csv


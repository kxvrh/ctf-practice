#!/bin/bash
while true  
do  
	find /var/www/html/ -cmin -10 -type f | xargs rm -rf
	sleep 1
done
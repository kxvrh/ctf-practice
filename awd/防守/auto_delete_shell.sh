#!/bin/bash
while true  
do  
	#find /var/www/html/ -cmin -10 -type f | xargs rm -rf
	find /var/www/html/ -name .333.php | xargs rm -rf
	sleep 0.01
done

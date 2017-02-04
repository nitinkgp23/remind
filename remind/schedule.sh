#!/bin/sh 

#var message = $1
#write out current crontab
crontab -l > temp

#echo new cron into cron file
echo "$3 $2 * * * ~/remind/remind/notify.sh $1" >> temp

#install new cron file
crontab temp
rm temp

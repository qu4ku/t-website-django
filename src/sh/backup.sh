#!/bin/bash
# cron 
# 0 1 * * * bash  /var/www/trenerindywidualnyonline/current/src/sh/backup.sh

source /var/www/trenerindywidualnyonline/current/env/bin/activate
python /var/www/trenerindywidualnyonline/current/src/manage.py dbbackup -s trenerindywidualnyonline --settings=project.settings.production
python /var/www/trenerindywidualnyonline/current/src/manage.py mediabackup -s trenerindywidualnyonline --settings=project.settings.production 
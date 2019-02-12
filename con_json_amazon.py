
# -*- coding: utf-8 -*-


## import libraries
import psycopg2
from pyathena import connect
import json

## open json file as config
with open('example_config_amazon.json') as json_data_file:
    data = json.load(json_data_file)

## create the connections with amazon(redshift and/or athena)
conn= psycopg2.connect(
dbname=data["redshift"]["dbname"],
host=data["redshift"]["host"], 
port=data["redshift"]["port"], 
user=data["redshift"]["user"],
password=data["redshift"]["pass"])

conn2= connect(
aws_access_key_id=data["athena"]["aws_access_key_id"],
aws_secret_access_key=data["athena"]["aws_secret_access_key"],
s3_staging_dir=data["athena"]["s3_staging_dir"],
region_name=data["athena"]["region_name"])

## Create cursors
cur_redshift = conn.cursor()
cur_athena = conn2.cursor()


## tasks and queries that you need!


## closing cursors
cur_redshift.close()
cur_athena.close()

## closing connections
conn.close()
conn2.close()

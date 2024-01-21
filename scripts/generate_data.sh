#!/bin/bash

tsbs_generate_data --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-02-12T00:00:00Z" --log-interval="10s" --format="influx" | gzip > ./datasets/influx_big.gz
tsbs_generate_data --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-02-12T00:00:00Z" --log-interval="10s" --format="timescaledb" | gzip > ./datasets/timescale_big.gz
tsbs_generate_data --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-01-10T08:00:00Z" --log-interval="10s" --format="influx" | gzip > ./datasets/influx_medium.gz
tsbs_generate_data --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-01-10T08:00:00Z" --log-interval="10s" --format="timescaledb" | gzip > ./datasets/timescale_medium.gz
tsbs_generate_data --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-01-02T13:45:00Z" --log-interval="10s" --format="influx" | gzip > ./datasets/influx_small.gz
tsbs_generate_data --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-01-02T13:45:00Z" --log-interval="10s" --format="timescaledb" | gzip > ./datasets/timescale_small.gz

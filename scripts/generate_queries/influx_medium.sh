#!/bin/bash

# Define the array
query_types=(
	"single-groupby-1-1-1"
	"single-groupby-1-1-12" 
	"single-groupby-1-8-1" 
	"single-groupby-5-1-1" 
	"single-groupby-5-1-12" 
	"single-groupby-5-8-1" 
	"cpu-max-all-1" 
	"cpu-max-all-8" 
	"double-groupby-1" 
	"double-groupby-5" 
	"double-groupby-all" 
	"high-cpu-all" 
	"high-cpu-1" 
	"lastpoint" 
	"groupby-orderby-limit"
)

# Loop over the array
for query_type in "${query_types[@]}"
do
  # Run the command with the current query type and redirect output to a gzip file
  /home/user/go/bin/tsbs_generate_queries --use-case="devops" --seed=123 --scale=10 --timestamp-start="2016-01-01T00:00:00Z" --timestamp-end="2016-01-10T08:00:01Z" --queries=1000 --query-type="$query_type" --format="influx" | gzip > "/home/user/go/src/tsbs/queries/influx_medium/influx_${query_type}.gz"
done

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

  /usr/bin/time -v sh -c "cat /home/user/go/src/tsbs/queries/influx_big/influx_${query_type}.gz | gunzip | /home/user/go/bin/tsbs_run_queries_influx --workers=2 --db-name=big"
done

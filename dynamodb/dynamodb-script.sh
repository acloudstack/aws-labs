#!/usr/bin/env bash

for i in {2..10}
 do
  val=${RANDOM}
  t=2
  # Insert Items
  echo -e "\n\n-=-=- Insert Movie:${i} and Retrieve after ${t} Seconds -=-=-"
  aws dynamodb put-item --table-name Movie --item '{"ID": {"S":"'${i}'"},"Title": {"S":"Title '${val}'"}, "Year": {"S":"2021"}}' --region us-east-1 --profile devuser-mycloudstack
  sleep ${t}
  # Read Items
  time aws dynamodb get-item --table-name Movie --key '{"ID": {"S":"'${i}'"},"Title": {"S":"Title '${val}'"}}' --region us-west-2 --profile devuser-mycloudstack
 done

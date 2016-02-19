#!/usr/local/bin/bash
mongoimport -d bpotinen -c movie_data --type csv --file /home/bpotinen/nosql/ass4/scripts/submit/data/title_out.csv --headerline

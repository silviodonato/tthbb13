#!/bin/bash

for site in T2_EE_Estonia T3_CH_PSI; do
	python ~/util/data_replica.py --delete --from LOCAL --to $site to-copy-step1.txt /store/user/jpata/tth/nov19_3a4602f/
done
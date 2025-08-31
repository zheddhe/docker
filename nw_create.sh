#!/bin/bash
docker network create \
	--subnet ${3:-172.50.0.0/16} \
	--gateway ${2:-172.50.0.1} \
	${1:-first_network}
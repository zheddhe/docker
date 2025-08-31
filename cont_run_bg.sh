#!/bin/bash
# lancement en -d ou --detach (background)
docker container run --detach \
	--name ${2:-first_container} \
	${1:-first_image}
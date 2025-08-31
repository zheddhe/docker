#!/bin/bash
# lancement en -d ou --detach (background)
# montage d'un docker volume avec --mount
docker container run --detach \
	--mount type=volume,src=${3:-first_named_volume},dst=${4:-/home/first_folder} \
	--name ${2:-first_container} \
	${1:-first_image}

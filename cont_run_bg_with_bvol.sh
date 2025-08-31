#!/bin/bash
# lancement en -d ou --detach (background)
# utilisation d'un bind volume (sur l'hôte) avec -v ou --volume
docker container run --detach \
	-v ${3:-~/github-docker/data/}:/app/data/ \
	--name "${2:-first_container}" \
	"${1:-first_image}"

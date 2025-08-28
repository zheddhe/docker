#!/bin/bash
# lancement en --detach (background)
docker container run -d \
	"${1:-first_image}" \
	--name "${2:-first_container}" \
	-v "${3:-~/github-docker/data/}:/app/data/"
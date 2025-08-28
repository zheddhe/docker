#!/bin/bash
# lancement en --detach (background)
docker container run -d \
	-v "${3:-~/github-docker/data/}:/app/data/" \
	--name "${2:-first_container}" \
	"${1:-first_image}"

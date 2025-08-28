#!/bin/bash
docker container run \
	--name "${2:-first_container}" \
	"${1:-first_image}"
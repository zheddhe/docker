#!/bin/bash
# build en précisant le nom de l'image et son tag avec -t ou --tag
docker image save \
	--output ${2:-first_image.tar} \
	${1:-first_image}
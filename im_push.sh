#!/bin/bash
# build en précisant le nom de l'image et son tag avec -t ou --tag
docker image push \
	"${1:-zheddhe/first_image}"

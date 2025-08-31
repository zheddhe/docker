#!/bin/bash
# en force (-f ou --force)
docker image rm --force \
	${1:-first_image}
#!/bin/bash
docker container run -d --name ${2:-first_container} -v ${3:-~/github-docker/data/}:/app/data/ ${1:-first_image}
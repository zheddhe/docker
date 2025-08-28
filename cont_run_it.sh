#!/bin/bash
docker container run -it --name ${2:-first_container} ${1:-first_image}
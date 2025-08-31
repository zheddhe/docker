#!/bin/bash
docker container exec \
	${1:-first_container} \
	bash
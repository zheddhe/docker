#!/bin/bash
docker volume inspect \
	${1:-first_named_volume}
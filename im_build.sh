#!/bin/bash
# build en précisant le nom de l'image et son tag avec -t ou --tag
docker image build .\
	--tag ${1:-first_image:latest}
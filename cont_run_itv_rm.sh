#!/bin/bash
# en interactif (-it)
# avec forçage de la suppression du container en fin d'exécution (-rm)
docker container run -it -rm --name ${2:-first_container} ${1:-first_image}
#!/bin/bash
# en interactif (-it)
# avec forçage de la suppression du container en fin d'exécution (-rm)
# + tous les arguments optionnels
docker container run -it -rm \
	"${1:-first_image}" \
	--name "${2:-first_container}" \
	"${@:3}"
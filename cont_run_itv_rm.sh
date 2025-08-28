#!/bin/bash
# en interactif (-it)
# avec forçage de la suppression du container en fin d'exécution (-rm)
# + tous les arguments optionnels à partir du 3eme (@:3) par exemple
# => variable d'env : 
#	-e "ma_variable='bonjour le monde'"
docker container run -it --rm \
	"${@:3}" \
	"${1:-first_image}" \
	--name "${2:-first_container}"
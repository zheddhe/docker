#!/bin/bash
# en interactif (-it)
# avec forçage de la suppression du container en fin d'exécution (-rm)
# + tous les arguments optionnels à partir du 3eme (@:3) par exemple
# => env variable : 
#	-e "first_variable='bonjour le monde'"
# => network : 
#	-n "first_network"
docker container run -it --rm \
	"${@:3}" \
	--name "${2:-first_container}" \
	"${1:-first_image}"
	# les commandes à envoyer au container sont à placer ici
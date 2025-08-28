#!/bin/bash
# en interactif (-it)
# avec forçage de la suppression du container en fin d'exécution (-rm)
# + tous les arguments optionnels à partir du 3eme (@:3) par exemple
# => env variable -e ou --env : 
#	--env "first_variable='bonjour le monde'"
# => network --net ou --network : 
#	--network "first_network"
# => port publish -p ou --publish (format host:container): 
#	--publish 9200:9200
docker container run -it --rm \
	"${@:3}" \
	--name "${2:-first_container}" \
	"${1:-first_image}"
	# les commandes à envoyer au container sont à placer ici
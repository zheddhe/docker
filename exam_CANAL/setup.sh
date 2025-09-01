# construction de l'image pour les tests authentication
docker image build ./authentication -t my_authentication_test_image:1.0.0

# construction de l'image pour les tests authentication
docker image build ./authorization -t my_authorization_test_image:1.0.0

# construction de l'image pour les tests content
docker image build ./content -t my_content_test_image:1.0.0

### Lancement en mode DOCKER-CLI
# creation d'un reseau partagé permettant la résolution par nom de domaine (le bridge par défaut ne le permet que par IP)
docker network create my_network

# démarrage du container fastapi qui nous est donné
# - FINAL : détaché / suppression une fois terminé / reseau
docker container run -d --rm \
	-p 8000:8000 \
	--network my_network \
	--name my_fastapi_container \
	datascientest/fastapi:1.0.0

# lancement du container basé sur l'image associée pour les tests authentication
# - FINAL : detaché / bind volume logs / suppression une fois terminé
docker container run -d --rm \
	--volume ./logs:/tests/logs \
	--network my_network \
	--name my_authentication_test_container \
	my_authentication_test_image:1.0.0
# - DEBUG : interactif / bind volume logs / suppression une fois terminé / surcharge de commande bash
# docker container run -it --rm \
# 	--volume ./logs:/tests/logs \
#	--network my_network \
# 	--name my_authentication_test_container \
# 	my_authentication_test_image:1.0.0 bash

# lancement du container basé sur l'image associée pour les tests authorization
# - FINAL : detaché / bind volume logs / suppression une fois terminé
docker container run -d --rm \
	--volume ./logs:/tests/logs \
	--network my_network \
	--name my_authorization_test_container \
	my_authorization_test_image:1.0.0
# - DEBUG : interactif / bind volume logs / suppression une fois terminé / surcharge de commande bash
# docker container run -it --rm \
# 	--volume ./logs:/tests/logs \
#	--network my_network \
# 	--name my_authorization_test_container \
# 	my_authorization_test_image:1.0.0 bash

# lancement du container basé sur l'image associée pour les tests content
# - FINAL : detaché / bind volume logs / suppression une fois terminé
docker container run -d --rm \
	--volume ./logs:/tests/logs \
	--network my_network \
	--name my_content_test_container \
	my_content_test_image:1.0.0
# - DEBUG : interactif / bind volume logs / suppression une fois terminé / surcharge de commande bash
# docker container run -it --rm \
# 	--volume ./logs:/tests/logs \
#	--network my_network \
# 	--name my_content_test_container \
# 	my_content_test_image:1.0.0 bash

# arrêt du container fastapi
docker container stop my_fastapi_container

# suppression du reseau pour le mode CLI (le docker compose créé son propre sous réseau dans le YAML)
docker network remove my_network

### Lancement en mode DOCKER-COMPOSE
# lancement des container avec docker compose en arrière plan (-d)
docker compose up -d
# arrêt et suppression des containers/network via docker compose 
# idéalement on mettrait plus qu'un délai de grâce mais un vrai évènement
# pour vérifier l'extinction (si par exemple les containers de test n'ont pas
# terminé)
docker compose down --timeout 10
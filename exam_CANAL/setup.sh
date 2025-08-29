# construction de l'image pour les tests authentication
docker image build ./authentication -t my_authentication_test_image:1.0.0

# lancement du container basé sur l'image associée pour les tests authentication
# - FINAL : detaché / bind volume logs / suppression une fois terminé
# docker container run -d --rm \
# 	--volume ./logs:/tests/logs \
# 	--name my_authentication_test_container \
# 	my_authentication_test_image:1.0.0
# - DEBUG : interactif /bind volume logs / suppression une fois terminé / surcharge de commande bash
# docker container run -it --rm \
# 	--volume ./logs:/tests/logs \
# 	--name my_authentication_test_container \
# 	my_authentication_test_image:1.0.0 bash

# construction de l'image pour les tests authentication
docker image build ./authorization -t my_authorization_test_image:1.0.0

# lancement du container basé sur l'image associée pour les tests authorization
# - FINAL : detaché / bind volume logs / suppression une fois terminé
# docker container run -d --rm \
# 	--volume ./logs:/tests/logs \
# 	--name my_authorization_test_container \
# 	my_authorization_test_image:1.0.0
# - DEBUG : interactif /bind volume logs / suppression une fois terminé / surcharge de commande bash
# docker container run -it --rm \
# 	--volume ./logs:/tests/logs \
# 	--name my_authorization_test_container \
# 	my_authorization_test_image:1.0.0 bash

# construction de l'image pour les tests content
docker image build ./content -t my_content_test_image:1.0.0

# lancement du container basé sur l'image associée pour les tests content
# - FINAL : detaché / bind volume logs / suppression une fois terminé
# docker container run -d --rm \
# 	--volume ./logs:/tests/logs \
# 	--name my_content_test_container \
# 	my_content_test_image:1.0.0
# - DEBUG : interactif /bind volume logs / suppression une fois terminé / surcharge de commande bash
# docker container run -it --rm \
# 	--volume ./logs:/tests/logs \
# 	--name my_content_test_container \
# 	my_content_test_image:1.0.0 bash

# lancement des container avec docker compose en arrière plan (-d)
docker compose up -d
# arrêt et suppression des containers/network via docker compose 
# idéalement on mettrait plus qu'un délai de grâce mais un vrai évènement
# pour vérifier l'extinction (si par exemple les containers de test n'ont pas
# terminé)
docker compose down --timeout 10
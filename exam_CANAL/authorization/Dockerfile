# choix d'une image python pure légère (on pourra quand même lancer en interactif avec bash)
FROM python:3.12-slim

# répertoire de travail
WORKDIR /tests

# installation de requests
RUN pip install --no-cache-dir requests

ENV LOG=1
# ENV API_ADDRESS="172.17.0.2"
# résolution par nom de domaine (nom du container) en le déployant sur un reseau dédié "my_network"
# son --name sera "my_fastapi_container"
ENV API_ADDRESS="my_fastapi_container"
ENV API_PORT="8000"

# copier le fichier python de tests dans WORKDIR directement
COPY ./*.py .

# dossier prévu pour les logs
VOLUME ["/tests/logs"]

# lancer le fichier de test avec python
CMD ["python", "test_authorization.py"]
#Utilisez une image de base - dans ce cas, Python 3.8
FROM python:3.8.10

#Définissez le répertoire de travail
WORKDIR /app

#Copiez les fichiers de votre application dans l'image - dans ce cas, un script python 
COPY app.py /app/
COPY requirements.txt /app/

#Exécutez des commandes dans l'environnement de construction de l'image. Il s'agit généralement d'installation de logiciels ou de librairies.
RUN pip install -r requirements.txt

#Exécutez une commande lorsque le conteneur démarre - dans ce cas, le script **'app.py'** qui se trouve dans le même dossier que le fichier Dockerfile
CMD ["python", "app.py"]
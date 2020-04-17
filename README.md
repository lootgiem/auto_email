-------------------- INITIALISATION ----------------------

Installer le packages suivant :
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

1* - Pour utiliser l'api gmail il faut faire le process qui suit avec un compte gmail qui est le votre (pas celui de l'école)... (une astuce est dispo à la fin pour utiliser l'adresse de l'école pour l'envoi des emails)

1 - Rendez vous sur : https://developers.google.com/gmail/api/quickstart/python et cliquer sur "Enable the Gmail API" à la fin du setup cliquer sur "DOWNLOAD CLIENT CONFIGURATION"

2 - Vous venez de télécharger un fichier "credentials.json" qu'il faut placer dans le dossier "config_files" du projet.

3 - Ensuite lancer le scrypt avec la commande python : "python main.py"

4 - Dans la console on vous demandera lors du premier lancement de cliquer sur un lien (il vous permettra d'autoriser l'accés de l'API Gmail à l'envoi d'emails), il suffit de suivre les étapes.

5 - FINI :D

-------------------- UTILISATION -------------------------

emails.csv : fichier contenant les emails à envoyés, ainsi que la configuration associé aux emails.

emails_format.csv : fichier contenant les formats d'email associé aux sociétés qui figure en premiere colonne et qui doivent être reprise dans la colonne societe de "emails.csv" pour faire la liaison.

1 - Comprendre les templates :

2 - Comprendre les attachments :

3 - Comprendre la génération d'emails :





from hashlib import sha512
import getpass
import json


#creation et hashage du mot de passe de reference

mdp = getpass.getpass('Mot de passe chifré: ')




#entree et hashage du mdp utilisateur 

user_mdp = getpass.getpass('Votre mot de passe: ')

user_mdp = user_mdp.encode()

user_mdp_sign = sha512(user_mdp).hexdigest()
print (user_mdp_sign)

adresseEnvoyeur = "0x214989565878995789759964"
adresseReceveur = "0x555555555555555555555555"

#comparaison du mdp entré par l'utilisateur au mdp de reference

user_message = getpass.getpass('Votre message: ')

user_message_encode = user_message.encode()

user_message_sign = sha512(user_message_encode).hexdigest()
print (user_message_sign)


crypto = getpass.getpass('Nombre de Eco: ')

block = {"Envoyeur": adresseEnvoyeur, "Receveur": adresseReceveur, "Message_chifre": user_message_sign, "Message": user_message, "Ecoria": crypto}

print (block)

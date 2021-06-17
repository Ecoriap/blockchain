from hashlib import sha512
import getpass


#creation et hashage du mot de passe de reference

mdp = getpass.getpass('Mot de passe chifré: ')




#entree et hashage du mdp utilisateur 

user_mdp = getpass.getpass('Votre mot de passe: ')

user_mdp = user_mdp.encode()

user_mdp_sign = sha512(user_mdp).hexdigest()
print (user_mdp_sign)



#comparaison du mdp entré par l'utilisateur au mdp de reference

user_message = getpass.getpass('Votre message: ')

user_message = user_message.encode()

user_message_sign = sha512(user_message).hexdigest()
print (user_message_sign)

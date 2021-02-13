from datetime import datetime
import instaloader

# Carrega a lib e faz login com a conta desejada #
L = instaloader.Instaloader()
L.login('*** SEU USER DO INSTA ***', '*** SUA SENHA ***')

# Carrega os dados de seguidores e seguindo do perfil escolhido #
followers = instaloader.Profile.from_username(L.context, "pycodebr").get_followers()
followees = instaloader.Profile.from_username(L.context, "pycodebr").get_followees()

# Mostra resultados #
print('\n')
print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followees._data['count']))
print('\n\n')
print('Lista e informações de seguidores:')
print('\n')
print(followers._data['edges'])
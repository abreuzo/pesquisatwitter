#-*- coding: utf-8 -*-
import twitter
import pprint
import tweepy
 
api = twitter.Api(consumer_key='0eVkfEdt4tt3YoL65TWuPC1rE',
                      consumer_secret='nmrWOaI4hDIClqRwxSAl7X0GyBOKY040sO5xd66gGjYBSfPecZ',
                      access_token_key='3001937488-vP0lhtFM2klYyKONE0mOzGItlueVOcnWxt9AOEN',
                      access_token_secret='3Yv9waMlFsQ15VxSC7yIFzAx0qWpPjGFMvIt6sJrBfRy5')
 
api.VerifyCredentials()
 
#Agora que voce conseguiu autenticar, vamos realizar uma busca simples pela palavra ladrao trazendo apenas os ultimos 10 resultados:

status_list = api.GetSearch(
    geocode=None, term=u"lava jato", since_id=None,
    lang="pt", count=10, result_type="recent"
)

print(status_list[5])
input()
for key in status_list[5]:
	print(status_list[5][key])



'''
arq = open("teste.txt", "w")
for e in lista:
	e = str(e)
	arq.writelines(e)

arq.close()

'''
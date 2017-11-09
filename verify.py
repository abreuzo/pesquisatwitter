#-*- coding: utf-8 -*-
import twitter
import pprint
 
api = twitter.Api(consumer_key='0eVkfEdt4tt3YoL65TWuPC1rE',
                      consumer_secret='nmrWOaI4hDIClqRwxSAl7X0GyBOKY040sO5xd66gGjYBSfPecZ',
                      access_token_key='3001937488-vP0lhtFM2klYyKONE0mOzGItlueVOcnWxt9AOEN',
                      access_token_secret='3Yv9waMlFsQ15VxSC7yIFzAx0qWpPjGFMvIt6sJrBfRy5')
 
api.VerifyCredentials()
 
status_list = api.GetSearch(
    geocode=None, term=u"ladrao", since_id=None,
    lang="pt", count=10, result_type="recent"
)
 
print(status_list)

arq = open("teste_bd.txt", "w")
print(arq)
for e in status_list:
	arq.writelines(e)
arq.close()
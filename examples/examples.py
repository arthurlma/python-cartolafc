import cartolafc

api = cartolafc.Api(email='email@email.com', password='s3nh4', attempts=5)

print api.amigos()
print api.clubes()
print api.liga(nome='Virtus Premier League')
print api.liga(slug='virtus-premier-league')
print api.ligas(query='Virtus')
print api.mercado()
print api.status_mercado()
# print api.parciais()
print api.pontuacao_atleta(81682)
print api.pos_rodada_destaques()
print api.time(id=471815)
print api.time(nome='Falydos FC')
print api.time(slug='falydos-fc')
print api.time_logado()
print api.times(query='Faly')

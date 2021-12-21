from dominio import Usuario, Lance, Leilao, Avaliador


ana = Usuario('Ana')
julia = Usuario('Júlia')
maria = Usuario('Maria')

lance_julia = Lance(julia, 135)
lance_maria = Lance(maria, 333.33)
lance_ana = Lance(ana, 125.50)

leilao = Leilao('Forninho')

leilao.propoe(lance_ana)
leilao.propoe(lance_maria)
leilao.propoe(lance_julia)

for i in leilao.lances:
    print(f'O cliente {i.usuario.nome} deu o lance de RS {i.valor:.2f}')


avaliador = Avaliador()

avaliador.avalia(leilao)
print(f'maior lance {avaliador.maior_lance}\nmenor lance {avaliador.menor_lance}')

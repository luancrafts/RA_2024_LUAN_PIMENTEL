transformacoes_personagens = {
    'Goku': ['Super Saiyajin', 'Super Saiyajin Deus', 'Super Saiyajin Blue', 'Ultra Instinto'],
    'Vegeta': ['Super Saiyajin', 'Super Saiyajin Blue', 'Ultra Instinto'],
    'Gohan': ['Super Saiyajin', 'Ultimate Gohan'],
    'Trunks': ['Super Saiyajin', 'Super Saiyajin Rage'],
    'Piccolo': ['Namekuseijin', 'Super Namekuseijin'],
    'Freeza': ['Forma Final', 'Golden Freeza'],
    'Cell': ['Forma Imperfeita', 'Forma Perfeita', 'Super Perfect Cell'],
    'Majin Boo': ['Majin Boo Gordo', 'Majin Boo Magro', 'Majin Boo Puro']
}

transformacoes_unicas = set()

for transformacoes in transformacoes_personagens.values():
    transformacoes_unicas.update(transformacoes)

print(transformacoes_unicas)
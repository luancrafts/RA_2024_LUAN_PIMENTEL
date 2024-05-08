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

personagem = 'Goku'
transformacao = 'Super Saiyajin 3'

print(transformacao in transformacoes_personagens.get(personagem, []))
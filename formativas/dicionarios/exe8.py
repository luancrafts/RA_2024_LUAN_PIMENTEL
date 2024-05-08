
tecnicas_luta_personagens = {
    'Goku': ['Kamehameha', 'Genki Dama', 'Instant Transmission', 'Spirit Bomb'],
    'Vegeta': ['Final Flash', 'Galick Gun', 'Big Bang Attack'],
    'Gohan': ['Masenko', 'Kamehameha', 'Father-Son Kamehameha'],
    'Trunks': ['Burning Attack', 'Finish Buster', 'Sword of Hope'],
    'Piccolo': ['Special Beam Cannon', 'Hellzone Grenade', 'Light Grenade'],
    'Freeza': ['Death Beam', 'Death Ball', 'Supernova'],
    'Cell': ['Kamehameha', 'Solar Kamehameha', 'Self-Destruct'],
    'Majin Boo': ['Chocolate Beam', 'Vanishing Beam', 'Boo Ball']
}

personagem = 'Vegeta'
tecnica = 'Final Flash'

tecnicas_luta_personagens[personagem].remove(tecnica)
print(f"A técnica '{tecnica}' foi removida para o personagem '{personagem}'.")
print(tecnicas_luta_personagens)
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

personagem = 'Goku'
nova_tecnica = 'Kaio-Ken'

if personagem in tecnicas_luta_personagens:
    tecnicas_luta_personagens[personagem].append(nova_tecnica)
    print(f"A nova técnica '{nova_tecnica}' foi adicionada para o personagem '{personagem}'.")
else:
    print(f"Não foi possível encontrar o personagem '{personagem}'.")

print(tecnicas_luta_personagens)
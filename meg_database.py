import random

def generate_map(size=5):
    directions = ['N', 'S', 'E', 'W']
    map_grid = [[' ' for _ in range(size)] for _ in range(size)]
    x, y = size // 2, size // 2
    map_grid[y][x] = 'S'  # S for Start
    
    for _ in range(size * 2):
        direction = random.choice(directions)
        if direction == 'N' and y > 0:
            y -= 1
        elif direction == 'S' and y < size - 1:
            y += 1
        elif direction == 'E' and x < size - 1:
            x += 1
        elif direction == 'W' and x > 0:
            x -= 1
        
        if map_grid[y][x] == ' ':
            map_grid[y][x] = 'R'  # R for Room
    
    map_grid[y][x] = 'E'  # E for Exit
    return map_grid

meg_database = {
    "Level 0": {
        "nome_ufficiale": "The Lobby",
        "classe_di_sicurezza": "C",
        "descrizione_breve": "Vasto labirinto di uffici vuoti con moquette umida e pareti gialle.",
        "consigli": "Mantieni la calma, segui le pareti, cerca anomalie che potrebbero indicare un'uscita.",
        "entità_note": ["Hound", "Faceling"],
        "risorse": "Acqua almond occasionale, scorte di cibo rare.",
        "mappa": generate_map()
    },
    "Level 1": {
        "nome_ufficiale": "Habitable Zone",
        "classe_di_sicurezza": "B",
        "descrizione_breve": "Vasto magazzino buio con scaffali e macchinari arrugginiti.",
        "consigli": "Fai attenzione ai rumori metallici, potrebbero indicare entità o macchinari pericolosi.",
        "entità_note": ["Smiler", "Duller"],
        "risorse": "Strumenti e materiali vari, possibili nascondigli.",
        "mappa": generate_map()
    },
    "Level 2": {
        "nome_ufficiale": "Pipe Dreams",
        "classe_di_sicurezza": "B",
        "descrizione_breve": "Interminabile corridoio con porte numerate e tubi che corrono lungo il soffitto.",
        "consigli": "Non fidarti dei numeri sulle porte, potrebbero cambiare. Segui i tubi per orientarti.",
        "entità_note": ["Hound", "Smiler"],
        "risorse": "Occasionali scorte di cibo e acqua nascoste dietro le porte.",
        "mappa": generate_map()
    }
}

def get_meg_info(level):
    if level in meg_database:
        info = meg_database[level]
        map_str = "\n".join([" ".join(row) for row in info['mappa']])
        return f"""
Informazioni M.E.G. per {level}:
Nome ufficiale: {info['nome_ufficiale']}
Classe di sicurezza: {info['classe_di_sicurezza']}
Descrizione: {info['descrizione_breve']}
Consigli: {info['consigli']}
Entità note: {', '.join(info['entità_note'])}
Risorse: {info['risorse']}

Mappa del livello:
{map_str}
"""
    else:
        return f"Nessuna informazione disponibile nel database M.E.G. per {level}."

levels = {
    "Level 0": {
        "description": "vasto labirinto di uffici vuoti con moquette umida e pareti gialle",
        "events": [
            "Le luci sfarfallano improvvisamente.",
            "Un ronzio costante riempie l'aria.",
            "L'Agente X sente un odore di muffa.",
            "Un'ombra sembra muoversi in lontananza.",
            "Il pavimento scricchiola sotto i piedi dell'Agente X."
        ],
        "entities": ["Hound", "Faceling"],
        "exits": ["Level 1", "The End"]
    },
    "Level 1": {
        "description": "magazzino buio pieno di scaffali e macchinari arrugginiti",
        "events": [
            "Un rumore metallico risuona in lontananza.",
            "L'Agente X vede una luce intermittente in un angolo.",
            "Un freddo improvviso attraversa la stanza.",
            "Si sente un sussurro incomprensibile.",
            "L'Agente X inciampa su un oggetto non identificato."
        ],
        "entities": ["Smiler", "Duller"],
        "exits": ["Level 0", "Level 2"]
    },
    "Level 2": {
        "description": "interminabile corridoio con porte numerate",
        "events": [
            "Una delle porte si apre leggermente da sola.",
            "L'Agente X sente passi dietro di sé, ma non c'è nessuno.",
            "I numeri sulle porte sembrano cambiare quando non li si guarda direttamente.",
            "Un'eco distante di una risata infantile risuona nel corridoio.",
            "L'Agente X nota che la sua ombra si muove in modo strano."
        ],
        "entities": ["Hound", "Smiler"],
        "exits": ["Level 1", "The End"]
    }
}

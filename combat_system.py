import random

class Entity:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(1, self.damage)

entities = {
    "Hound": Entity("Hound", 30, 10),
    "Faceling": Entity("Faceling", 20, 8),
    "Smiler": Entity("Smiler", 40, 15),
    "Duller": Entity("Duller", 25, 12),
}

def encounter_chance(room_type):
    if room_type == 'S':  # Start room
        return 0
    elif room_type == 'E':  # Exit room
        return 0.5
    else:  # Regular room
        return 0.2

def combat(entity):
    agent_health = 50
    print(f"Un {entity.name} attacca l'Agente X!")
    
    while agent_health > 0 and entity.health > 0:
        print(f"\nSalute dell'Agente X: {agent_health}")
        print(f"Salute del {entity.name}: {entity.health}")
        print("1. Ordina all'Agente X di attaccare")
        print("2. Ordina all'Agente X di difendersi")
        print("3. Ordina all'Agente X di tentare la fuga")
        
        choice = input("Quale ordine vuoi dare all'Agente X? ")
        
        if choice == "1":
            damage = random.randint(5, 15)
            entity.health -= damage
            print(f"L'Agente X ha inflitto {damage} danni al {entity.name}!")
        elif choice == "2":
            print("L'Agente X si prepara a difendersi.")
        elif choice == "3":
            if random.random() < 0.5:
                print("L'Agente X è riuscito a fuggire!")
                return True
            else:
                print("L'Agente X non è riuscito a fuggire!")
        else:
            print("Ordine non valido. L'Agente X perde il turno!")
        
        if entity.health <= 0:
            print(f"L'Agente X ha sconfitto il {entity.name}!")
            return True
        
        entity_damage = entity.attack()
        if choice == "2":
            entity_damage //= 2
        agent_health -= entity_damage
        print(f"Il {entity.name} ha inflitto {entity_damage} danni all'Agente X!")
    
    if agent_health <= 0:
        print("L'Agente X è stato sconfitto...")
        return False

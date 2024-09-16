import time
import random
from support_levels import levels
from meg_database import get_meg_info, meg_database
from combat_system import entities, encounter_chance, combat

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_input():
    return input("Comando: ").lower()

def random_event(current_level):
    return random.choice(levels[current_level]["events"])

def game():
    print_slow("Inizializzazione del sistema di comunicazione...")
    print_slow("Connessione stabilita con l'agente sul campo.")
    print_slow("\nBenvenuto, agente di supporto. Sei in contatto con l'Agente X, attualmente intrappolato nelle Backrooms.")
    print_slow("Il tuo compito è guidarlo verso l'uscita. Buona fortuna.")

    current_level = "Level 0"
    map_grid = meg_database[current_level]["mappa"]
    agent_pos = next((i, j) for i, row in enumerate(map_grid) for j, cell in enumerate(row) if cell == 'S')
    
    while True:
        current_room = map_grid[agent_pos[0]][agent_pos[1]]
        print_slow(f"\nL'Agente X si trova nel {current_level}, in una {levels[current_level]['description']}")
        print_slow(random_event(current_level))
        print_slow("\nCosa vuoi dire all'Agente X?")
        print_slow("1. Muoviti")
        print_slow("2. Cerca un'uscita")
        print_slow("3. Resta fermo e ascolta")
        print_slow("4. Consulta il database M.E.G.")
        print_slow("5. Termina la missione")

        choice = get_input()

        if choice == "1" or choice == "muoviti":
            print_slow("In quale direzione vuoi che l'Agente X si muova?")
            print_slow("N: Nord, S: Sud, E: Est, W: Ovest")
            direction = get_input().upper()
            if direction in ['N', 'S', 'E', 'W']:
                new_pos = list(agent_pos)
                if direction == 'N' and new_pos[0] > 0:
                    new_pos[0] -= 1
                elif direction == 'S' and new_pos[0] < len(map_grid) - 1:
                    new_pos[0] += 1
                elif direction == 'E' and new_pos[1] < len(map_grid[0]) - 1:
                    new_pos[1] += 1
                elif direction == 'W' and new_pos[1] > 0:
                    new_pos[1] -= 1
                
                if tuple(new_pos) != agent_pos:
                    agent_pos = tuple(new_pos)
                    print_slow(f"L'Agente X si è spostato verso {direction}.")
                    
                    if random.random() < encounter_chance(map_grid[agent_pos[0]][agent_pos[1]]):
                        entity = random.choice(list(entities.values()))
                        if not combat(entity):
                            print_slow("L'Agente X è stato sconfitto. Missione fallita.")
                            break
                else:
                    print_slow("L'Agente X non può muoversi in quella direzione.")
            else:
                print_slow("Direzione non valida.")
        elif choice == "2" or choice == "cerca un'uscita":
            if current_room == 'E':
                print_slow("Ottimo! L'Agente X ha trovato l'uscita da questo livello!")
                current_level = random.choice(levels[current_level]["exits"])
                if current_level == "The End":
                    print_slow("Hai guidato l'Agente X fuori dalle Backrooms! Missione compiuta!")
                    break
                else:
                    map_grid = meg_database[current_level]["mappa"]
                    agent_pos = next((i, j) for i, row in enumerate(map_grid) for j, cell in enumerate(row) if cell == 'S')
            else:
                print_slow("L'Agente X non riesce a trovare un'uscita in questa stanza.")
        elif choice == "3" or choice == "resta fermo e ascolta":
            print_slow("Hai detto all'Agente X di restare fermo e ascoltare.")
            print_slow(random_event(current_level))
        elif choice == "4" or choice == "consulta il database m.e.g.":
            print_slow("Stai consultando il database M.E.G. ...")
            print_slow(get_meg_info(current_level))
        elif choice == "5" or choice == "termina la missione":
            print_slow("Hai deciso di terminare la missione. L'Agente X rimarrà intrappolato nelle Backrooms per sempre.")
            break
        else:
            print_slow("Comando non riconosciuto. Ripeti.")

if __name__ == "__main__":
    game()

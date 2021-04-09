#! usr/bin/env python3
# coding: utf-8

import json
import random

def read_json_file(difficulty_letter):
    with open('calculs/parcours_' + difficulty_letter + '.json') as file:
        data = json.load(file)
    return data

def main():
    difficulte_tape = ''
    is_difficulty_correct = False

    print('')
    print('         Jeu de maths')
    print('')

    while is_difficulty_correct == False:
        print('Choisis un niveau de difficulté (tape la lettre indiquée après la flèche) :')
        print('  - Facile (additions et soustractions) ➡  F')
        print('  - Intermédiaire (multiplications et divisions) ➡  I')
        print('  - Difficile (fractions et nombres à virgule) ➡  D')

        difficulte_tape = input()

        if difficulte_tape == 'F' or difficulte_tape == 'I' or difficulte_tape =='D':
            is_difficulty_correct = True
        else:
            is_difficulty_correct = False
            print('')
            print('⚠ IL FAUT TAPER UNE DE CES LETTRES : "F", "I" OU "D", EN MAJUSCULES ! ⚠')
            print('')
    
    print('')
    print('Avant de jouer, quelques précisions :')
    print('  - Pas d\'espace entre les millions, les milliers et les unités,')
    print('  - Pour les nombres à virgule, il faut les écrire à l\'américaine : avec "." et pas avec ",".')
    print('Tout est O.K. ?')
    input()

    calculs = read_json_file(difficulte_tape)
    note = 0
    id_calcul = 1

    for a_calcul in calculs:
        calcul_choisi = random.randint(0, 2)

        print('')
        print('         Calcul n° {}'.format(id_calcul))
        print('')
        print(a_calcul[calcul_choisi]['calcul'])

        try:
            reponse_tape = float(input())

            if reponse_tape == a_calcul[calcul_choisi]['result']:
                print('Bravo, tu as réussi ce calcul 👏 !')
                note = note + 1
            else:
                print('Tu t\'est trompé 😓. Dommage, la bonne réponse était : {}'.format(a_calcul[calcul_choisi]['result']))
        except ValueError:
            print('IL FAUT TAPER UN NOMBRE 😡 !')

        id_calcul = id_calcul + 1

    print('')
    print('Ta note est de  : {}/{}'.format(note, id_calcul - 1))
    if note == 10:
        print('Super, c\'est un sans-faute 👏🎆 !')
    elif 10 > note > 4:
        print('C\'est super, tu y es presque 😊 !')
    elif 5 > note > 0:
        print('C\'est bof, la prochaine fois, il faudra faire un petit effort 😉.')
    elif note == 0:
        print('C\'EST UNE VERITABLE CATASTROPHE 👎😡 ! VA T\'ENTRAINER TOUT DE SUITE 👉 !')
    else:
        print('Désolé, il y a eu une petite erreur 😓...')

if __name__ == "__main__":
    main()

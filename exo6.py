#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        result = []
        for i in range(10):
            result.append(input(f"Entrez la valeur #{i+1}: "))
    else:
        result = values
    
    numbers = []#[number for number in result if str(number).isdigit()]
    strings = []#[string for string in result if not str(string).isdigit()]

    for value in values:
        if isinstance(value, str):
            if value.isdigit():
                numbers.append(value)
            else:
                strings.append(value)
        elif str(value)[0] == "-" and str(value)[1:].isdigit():
            numbers.append(value)
        elif str(value).isdigit():
            numbers.append(value)

    return sorted(numbers) + sorted(strings)


def anagrams(words: list = None) -> bool:
    if words is None:
        mots = [input("Premier mot: "), input("Deuxième mot: ")]
    else:
        mots = words
    return sorted(mots[0]) == sorted(mots[1])


def contains_doubles(items: list) -> bool:
    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = {}
    for student, grade in student_grades.items():
        average = sum(grade)/len(grade)

        if len(best_student) == 0 or list(best_student.values())[0] < average:
            best_student = {student: average}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    times_letters, result = {}, ""
    for letter in sentence:
        if letter.isalpha() and sentence.count(letter) > 4:
            times_letters[letter] = sentence.count(letter)
    
    keys_in_order = sorted(times_letters, key= times_letters.__getitem__, reverse = True)
    
    for key in keys_in_order:
        result += f"La lettre {key} apparait {times_letters[key]} fois\n"
    print(result)

    return keys_in_order


def get_recipes():
    # Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Quel est le nom de votre recette?\n")
    ingredients = input("Inscrivez les ingredients de votre recette en les séparants d'un espace:\n").split()
    return {name: ingredients}


def print_recipe(ingredients) -> None:
    # Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Quel est le nom de votre recette? ")
    if name in ingredients:
        print(ingredients[name])
    else:
        print(f"Cette recette n'existe pas\nVoici les recettes disponibles: {ingredients}")
        print_recipe(ingredients)
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()

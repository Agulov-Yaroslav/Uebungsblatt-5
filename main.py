#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""bungsblatt 05"""


# Aufgabe 1

def add_snake(snake, skill, template):
    """

    :param snake:
    :param skill:
    :param template:
    :return:
    """
    new_snake = (snake, skill)
    my_snakes = template.copy()
    my_snakes.append(new_snake)
    return my_snakes


# Aufgabe 2

def is_perfect_number(number):
    """

    :param number: eine Ganzzahl
    :type number: int
    :return: True, wenn die übergebene natürliche, positive Zahl
            eine vollkommene Zahl ist
    :rtype: bool
    """
    n = 1
    teilers = []
    if isinstance(number, int) and number > 0:
        while n < number:
            if number % n == 0:
                teilers.append(n)
            n += 1
        if sum(teilers) == number:
            return True
    return False


# Aufgabe 3

def append_square(number, numbers=None):
    """

    :param number:
    :param numbers: wenn nichts, dann leeres List
    :return:
    """
    number = number ** 2
    if numbers is None:
        return [number]
    numbers.append(number)
    return numbers


# Aufgabe 4

def factorial(number):
    """
    Python has a limit on the number of times a function can call itself recursively.
    Deswegen mache ich es lieber mit Hilfe der Schleife

    :param number:
    :type number: int
    :return: die Fakultät einer Zahl
    """
    n = 1
    fakult = 1
    while n <= number:
        fakult *= n
        n += 1
    return fakult


# Aufgabe 5

def euros_to_dollars(customers):
    """
    Der Fehler hier ist, dass customers.copy() nur eine flache Kopie des Dictionaries erstellt.
    Das bedeutet, dass zwar das Dictionary customers selbst kopiert wird,
    aber die Listen innerhalb der Werte des Dictionaries werden nicht kopiert.
    Ich habe den Modul copy benutzt und dies zu vermeiden


    :param customers: Rechnung in Währung Euro
    :type customers: dict
    :return: Rechnung in Währung Dollars
    :rtype: dict
    """
    import copy

    new_customers = copy.deepcopy(customers)

    # for name, rechnung in new_customers.items():
    #     i = 0
    #     while i < len(rechnung):
    #         rechnung[i] = rechnung[i] * 1.5
    #         print(rechnung[i])
    #         i += 1
    # return new_customers

    for name in new_customers:
        print(name)
        for index, euro in enumerate(new_customers[name]):
            new_customers[name][index] = euro * 1.5
    return new_customers


# Aufgabe 6

def print_random_chess_position():
    """
    das passierte wegen Namensüberschreibung von random
    Durch das erneute Zuweisen des Namens random
    zu einer Variablen wird das random-Modul überschrieben,
    deswegen sollen wir die Variablen anders nennen, um dies zu vermeiden
    :return:
    """
    import random

    horisontal= random.choice("ABCDEFGH")
    vertical = random.randint(1, 8)
    print("Horizontal: {}".format(horisontal))
    print("Vertikal: {}".format(vertical))


# Testaufrufe

if __name__ == "__main__":
    SNAKES = [("Cobra", "Venom"), ("Boa", "Constriction")]
    MY_SNAKES = add_snake("Rattlesnake", "Venom", SNAKES)
    print(MY_SNAKES)
    print(SNAKES)  # Unverändert

    print("27 ist eine perfekte Zahl:", is_perfect_number(27))
    print("28 ist eine perfekte Zahl:", is_perfect_number(28))

    print(append_square(7, numbers=[9, 4]))
    print(append_square(1, numbers=[]))
    print(append_square(2))
    print(append_square(3))
    NUMBERS = []
    print(append_square(4, NUMBERS))
    print(append_square(5, NUMBERS))

    print("Fakultät von 3 ist:", factorial(3))
    print("Fakultät von 5 ist:", factorial(5))

    CUSTOMER_EUROS = {"Charles": [27, 12], "Jacques": [31, 38]}
    CUSTOMER_DOLLARS = euros_to_dollars(CUSTOMER_EUROS)
    print("Rechnung in Währung Euro:")
    print(CUSTOMER_EUROS)
    print("Rechnung in Währung Dollar:")
    print(CUSTOMER_DOLLARS)

    print_random_chess_position()

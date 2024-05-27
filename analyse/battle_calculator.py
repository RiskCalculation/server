from random import randint


def simulate_battle(attacker_data, defender_data, iterations=1000):
    global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list
    a_siege_start = attacker_data['siege']
    b_siege_start = defender_data['siege']

    a_archers_start = attacker_data['archers']
    b_archers_start = defender_data['archers']

    a_cavalry_start = attacker_data['cavalry']
    b_cavalry_start = defender_data['cavalry']

    a_troops_start = attacker_data['infantry']
    b_troops_start = defender_data['infantry']

    a_list = []
    b_list = []

    attacker = 'a'

    siege_kill = 3
    siege_dices = 2
    archers_kill = 5
    archers_dices = 1
    cavalry_kill = 3
    cavalry_dices = 1

    attacker_bonus_a = 0
    attacker_bonus_b = 0

    if attacker == 'a':
        attacker_bonus_a += 1
    else:
        attacker_bonus_b += 1

    def numbers_to_list():
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        a_list = ['s'] * a_siege + ['c'] * a_cavalry + ['a'] * a_archers + ['t'] * a_troops
        b_list = ['s'] * b_siege + ['c'] * b_cavalry + ['a'] * b_archers + ['t'] * b_troops

    def list_to_numbers():
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        a_siege = sum(item == 's' for item in a_list)
        b_siege = sum(item == 's' for item in b_list)

        a_cavalry = sum(item == 'c' for item in a_list)
        b_cavalry = sum(item == 'c' for item in b_list)

        a_archers = sum(item == 'a' for item in a_list)
        b_archers = sum(item == 'a' for item in b_list)

        a_troops = sum(item == 't' for item in a_list)
        b_troops = sum(item == 't' for item in b_list)

    def do_damage(a_kills, b_kills):
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        if b_kills > 0:
            a_list = a_list[:-b_kills]
        if a_kills > 0:
            b_list = b_list[:-a_kills]

        list_to_numbers()

    def siege_attack():
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        if a_siege > 0 or b_siege > 0:
            a_dices = a_siege * siege_dices
            b_dices = b_siege * siege_dices

            a_roll = [randint(1, 6) for _ in range(a_dices)]
            b_roll = [randint(1, 6) for _ in range(b_dices)]

            a_kills = sum(dice >= siege_kill for dice in a_roll)
            b_kills = sum(dice >= siege_kill for dice in b_roll)

            do_damage(a_kills, b_kills)

    def archers_attack():
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        if a_archers > 0 or b_archers > 0:
            a_dices = a_archers * archers_dices
            b_dices = b_archers * archers_dices

            a_roll = [randint(1, 6) for _ in range(a_dices)]
            b_roll = [randint(1, 6) for _ in range(b_dices)]

            a_kills = sum(dice >= archers_kill for dice in a_roll)
            b_kills = sum(dice >= archers_kill for dice in b_roll)

            do_damage(a_kills, b_kills)

    def cavalry_attack():
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        if a_cavalry > 0 or b_cavalry > 0:
            a_dices = a_cavalry * cavalry_dices
            b_dices = b_cavalry * cavalry_dices

            a_roll = [randint(1, 6) for _ in range(a_dices)]
            b_roll = [randint(1, 6) for _ in range(b_dices)]

            a_kills = sum(dice >= cavalry_kill for dice in a_roll)
            b_kills = sum(dice >= cavalry_kill for dice in b_roll)

            do_damage(a_kills, b_kills)

    def all_attack():
        global a_siege, b_siege, a_archers, b_archers, a_cavalry, b_cavalry, a_troops, b_troops, a_list, b_list

        a_kills = 0
        b_kills = 0

        a_dices = min(2 + attacker_bonus_a, len(a_list))
        b_dices = min(2 + attacker_bonus_b, len(b_list))

        a_roll = [randint(1, 6) for _ in range(a_dices)]
        a_roll = sorted(a_roll, reverse=True)
        a_roll = a_roll[0:2]
        b_roll = [randint(1, 6) for _ in range(b_dices)]
        b_roll = sorted(b_roll, reverse=True)
        b_roll = b_roll[0:2]

        if a_roll[0] > b_roll[0]:
            a_kills += 1

        elif a_roll[0] == b_roll[0]:
            if attacker == 'a':
                b_kills += 1
            else:
                a_kills += 1

        else:
            b_kills += 1

        if min(len(a_roll), len(b_roll)) > 1:
            if a_roll[1] > b_roll[1]:
                a_kills += 1

            elif a_roll[0] == b_roll[0]:
                if attacker == 'a':
                    b_kills += 1
                else:
                    a_kills += 1

            else:
                b_kills += 1

        do_damage(a_kills, b_kills)

    wins_a = 0
    wins_b = 0

    for _ in range(iterations):
        a_siege = a_siege_start
        b_siege = b_siege_start

        a_archers = a_archers_start
        b_archers = b_archers_start

        a_cavalry = a_cavalry_start
        b_cavalry = b_cavalry_start

        a_troops = a_troops_start
        b_troops = b_troops_start

        a_list = []
        b_list = []

        numbers_to_list()

        while True:
            siege_attack()
            if len(a_list) <= 0 or len(b_list) <= 0:
                if len(a_list) > 0:
                    wins_a += 1
                elif len(b_list) > 0:
                    wins_b += 1
                break

            archers_attack()
            if len(a_list) <= 0 or len(b_list) <= 0:
                if len(a_list) > 0:
                    wins_a += 1
                elif len(b_list) > 0:
                    wins_b += 1
                break

            cavalry_attack()
            if len(a_list) <= 0 or len(b_list) <= 0:
                if len(a_list) > 0:
                    wins_a += 1
                elif len(b_list) > 0:
                    wins_b += 1
                break

            all_attack()
            if len(a_list) <= 0 or len(b_list) <= 0:
                if len(a_list) > 0:
                    wins_a += 1
                elif len(b_list) > 0:
                    wins_b += 1
                break

    a_wr = wins_a / iterations * 100
    b_wr = wins_b / iterations * 100
    draw_wr = (iterations - wins_a - wins_b) / iterations * 100
    return {
        'attacker_win_rate': a_wr,
        'defender_win_rate': b_wr,
        'draw_rate': draw_wr
    }

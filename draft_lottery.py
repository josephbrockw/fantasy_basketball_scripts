from random import choice
from tqdm import tqdm
from time import sleep

odds = [
    (1, 140),
    (2, 140),
    (3, 140),
    (4, 125),
    (5, 105),
    (6, 90),
    (7, 75),
    (8, 60),
    (9, 45),
    (10, 30),
    (11, 20),
    (12, 15),
]

def run_lottery():
    combinations = []
    order = []

    combinations = [[x[0]] * x[1] for x in odds]
    combinations = [item for sublist in combinations for item in sublist]

    for i in range(4):
        team = choice(combinations)
        order.append(team)
        combinations = [x for x in combinations if x != team]

    for i in odds:
        if i[0] in order:
            continue
        else:
            order.append(i[0])
    return order

def run_simulations():
    simulations = []
    s = 1000000
    for i in tqdm(range(s)):
        simulations.append(run_lottery())

    test = [
        [1, []],
        [2, []],
        [3, []],
        [4, []],
        [5, []],
        [6, []],
        [7, []],
        [8, []],
        [9, []],
        [10, []],
        [11, []],
        [12, []]
    ]

    for sim in tqdm(simulations):
        pick = False
        for i in range(len(sim)):
            test[i][1].append(sim.index(test[i][0]))

    def calculate_odds(sims, pick):
        not_pick = [x for x in sims if x > pick]
        return round(1 - (len(not_pick) / len(sims)), 3)

    print("standing: average pick")
    for i in test:
        print(f"{i[0]}: {sum(i[1]) / len(i[1])}")


    print("Simulations: ", len(simulations))

def draft_lottery(simulation=False):
    if simulation:
        run_simulations()
    else:
        order = run_lottery()
        draft = []
        for i, pick in enumerate(order):
            draft.append((i + 1, pick))
        draft.reverse()
        print("Pick | Team")
        print("-----------")
        for pick in draft:
            if pick[0] < 10:
                print(f"{pick[0]}    | {pick[1]}")
            else:
                print(f"{pick[0]}   | {pick[1]}")
            sleep(1)

import sys
try:
    if sys.argv[1] == "sim":
        draft_lottery(simulation=True)
except:
    draft_lottery()


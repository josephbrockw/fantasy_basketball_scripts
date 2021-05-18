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

# order = run_lottery()

# print(order)
# order.reverse()

# for i in range(len(order)):
#     print(f"{12 - i}: {order[i]}")
#     sleep(1)


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

joe = []

for sim in tqdm(simulations):
    pick = False
    for i in range(len(sim)):
        test[i][1].append(sim.index(test[i][0]))
        if sim[i] in [2, 4] and pick == False:
            joe.append(i + 1)
            pick = True

def calculate_odds(sims, pick):
    not_pick = [x for x in sims if x > pick]
    return round(1 - (len(not_pick) / len(sims)), 3)

print("standing: average pick")
for i in test:
    print(f"{i[0]}: {sum(i[1]) / len(i[1])}")


print("Simulations: ", len(joe))

print(f"Average Position: {sum(joe) / len(joe)}")
print(f"1: {calculate_odds(joe, 1)}")
print(f"2: {calculate_odds(joe, 2)}")
print(f"3: {calculate_odds(joe, 3)}")
print(f"4: {calculate_odds(joe, 4)}")
print(f"5: {calculate_odds(joe, 5)}")
print(f"6: {calculate_odds(joe, 6)}")
print(f"7: {calculate_odds(joe, 7)}")
print(f"8: {calculate_odds(joe, 8)}")
print(f"9: {calculate_odds(joe, 9)}")
print(f"10: {calculate_odds(joe, 10)}")
print(f"11: {calculate_odds(joe, 11)}")
print(f"12: {calculate_odds(joe, 12)}")


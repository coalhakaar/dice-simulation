import random

# -- Variables -- #
ROLL_AMOUNT = 1_000_000

# -- Actual Stuff -- #
result = random.choices(
    ["Heads", "Side", "Tails"],
    weights=[
        random.uniform(49.992, 49.995), 
        random.uniform(0.010, 0.016), 
        random.uniform(49.992, 49.995)
    ],
    k=ROLL_AMOUNT
)

heads_count = 0
tails_count = 0
side_count = 0

for flip in result:
    if flip == "Heads":
        heads_count += 1
    elif flip == "Tails":
        tails_count += 1
    elif flip == "Side":
        side_count += 1
        

with open("output.txt", "w") as file:
    file.write("\n".join(result))

print("Script finished!")
print(f"Stats: \nHeads rolled {heads_count} times\nTails rolled {tails_count} times\nSide rolled {side_count} times")
# 1. WAP that you are in the team of 11 players find your name in that list using operators.

def team(target):
    players = []
    for i in range(11):
        member = input(f"Enter member {i+1} name of the team: ")
        players.append(member)
    if target in players:
        print("Match found.")
    else:
        print("Match not found.")

if __name__ == '__main__':
    # example call; change the target name as needed
    team("vkt")

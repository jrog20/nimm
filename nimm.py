"""
File: nimm.py
-------------------------
The ancient game of Nimm.
Two players start with a pile of 20 stones in the center. The players alternate turns,
each deciding to take 1 or 2 stones on their turn until all the stones are gone.
The last player to take a stone looses.
"""

def main():
    player = 1
    stones = 20
    while stones > 0:
        stones_remove = get_num_stones(stones, player)
        player = change_player(player)
        while stones_remove > 2 or stones_remove < 1:
            stones_remove = int(input('Please enter 1 or 2: '))
            print()
        stones -= stones_remove
    print(f'Player {player} wins!')

def get_num_stones(stones, player):
    print(f'There are {stones} stones left')
    stones_remove = int(input(f'Player {player} would you like to remove 1 or 2 stones? '))
    print()
    return stones_remove

def change_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

if __name__ == '__main__':
    main()

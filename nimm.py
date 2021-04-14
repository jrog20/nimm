"""
File: nimm.py
-------------------------
The ancient game of Nimm.
"""

def main():
    """
    Two players start with a pile of 20 stones in the center. The players alternate turns,
    each deciding to take 1 or 2 stones on their turn until all the stones are gone.
    The last player to take a stone looses.
    """
    player_num = 1
    num_stones = 20

    # Milestone 1: Start with 20 stones. Repeat the process of removing stones and printing
    # out how many stones are left until there are zero.
    while num_stones > 0:
        print("There are " + str(num_stones) + " stones left")
        num_stones_remove = int(input("Player " + str(player_num) + " would you like to remove 1 or 2 stones? "))
        print("")

        # Milestone 2: Create a variable of type int to keep track of whose turn it is.
        if player_num == 1:
            player_num += 1
        else:
            player_num -= 1

        # Milestone 3: Make sure that each turn only one or two stones are removed.
        while num_stones_remove > 2 or num_stones_remove < 1:
            num_stones_remove = int(input("Please enter 1 or 2: "))
            print("")

        num_stones -= num_stones_remove

    # When the last stone is drawn, the last player looses.
    print("Player " + str(player_num) + " wins!")


if __name__ == '__main__':
    main()

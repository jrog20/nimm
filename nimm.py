"""
File: nimm.py
-------------------------
The ancient game of Nimm.
Two players start with a pile of 20 stones in the center. The players alternate turns,
each deciding to take 1 or 2 stones on their turn until all the stones are gone.
The last player to take a stone looses.
"""

def main():
    player_num = 1
    num_stones = 20

    while num_stones > 0:
        print("There are", num_stones, "stones left")
        num_stones_remove = int(input("Player " + str(player_num) + " would you like to remove 1 or 2 stones? "))
        print("")

        if player_num == 1:
            player_num += 1
        else:
            player_num -= 1

        while num_stones_remove > 2 or num_stones_remove < 1:
            num_stones_remove = int(input("Please enter 1 or 2: "))
            print("")

        num_stones -= num_stones_remove

    print("Player " + str(player_num) + " wins!")


if __name__ == '__main__':
    main()

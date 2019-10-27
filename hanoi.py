import hanoi_viz


def number_of_disks():
    # prompts the user for the number of disks and kicks off the process
    number_of_disk = input("What is the number of disk (2-5)? \n")
    # Prompt the user to give you the number of disks. Prompt them repeatedly until they give you a valid number
    while True:
        # make sure that the user has provided an integer, not a float or a string or anything else
        # isdigit() checks whether the string consists of digits only
        if not number_of_disk.isdigit():
            print("Oops, that wasn't a number, please try again!")
            number_of_disk = input("What is the number of disk (2-5)? \n")
        else:
            # The integer they give you must be between 1 and 8 (inclusive)
            if 1 <= int(number_of_disk) <= 8:
                return number_of_disk
            else:
                print("Oops, that wasn't a number, please try again!")
                number_of_disk = input("What is the number of disk (2-5)? \n")


# A recursive function to move disks from one tower to another
# Define a recursive function that moves disks from one tower to another
# This function’s name is ​move_tower
# In addition to calling itself, this function should call the ​move_disk​ function in the hanoi_viz​ ​module
def move_tower(n_disk, source, target, middle, towers):
    if n_disk == 1:
        hanoi_viz.move_disk(source, target, towers)
    else:
        # To move ​n​ disks, you need to recursively move ​n-1​ disks and then move that last disk
        move_tower(n_disk - 1, source, middle, target, towers)
        hanoi_viz.move_disk(source, target, towers)
        move_tower(n_disk, middle, target, source, towers)


def main():
    # Choose names for the towers. These can be anything you like,
    # but keep them short or the illustrations won’t look right
    # we want to get both disks from A to B, and we use C as a helper
    source = "Tower_A"
    target = "Tower_B"
    middle = "Tower_C"
    number_of_disk = number_of_disks()
    # Call the given ​initialize_towers​ function before calling your own, recursive function
    towers = hanoi_viz.initialize_towers(number_of_disks(), source, target, middle)
    move_tower(number_of_disk, source, target, middle, towers)


main()

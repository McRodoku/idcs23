# Chance Salois
# 9/18/2023
# IDCS
# dice.py

# Modules imported
import random
import stdarray
import stdio
import sys

# Lowest and highest value of dice
dice_lowest_value = 1
dice_highest_value = 6
# Number of dice being thrown per trial
dice_thrown = 2


# Sets the lowest result possible to 2
dice_lowest_result = dice_lowest_value * dice_thrown
# Size of array needed to hold all results from a set of dice trials
dice_highest_result = dice_highest_value * dice_thrown + 1
# Added 1 is there because the index starts at 0. Otherwise, all my results will appear to be off by 1


def probability_formula():
    # Determines probability of each dice roll being any number in the array
    global probabilities
    probabilities = stdarray.create1D(13, 0.0)
    for i in range(1, 7):
        for j in range(1, 7):
            probabilities[i + j] += 1.0
    for k in range(2, 13):
        probabilities[k] /= 36.0


def run_dice_trials():
    # Tracks empirical results of dice roll totals from each trial
    global dice_counter
    dice_counter = stdarray.create1D(dice_highest_result, 0)

    # Trial loop that takes the dice roll results and stores the information
    for trial in range(0, num_trials):
        # Starting number of dice trials
        dice_total = 0
        # Takes the sum of both dice and counts it as a single trial
        for dice_roll in range(dice_thrown):
            # Determines the value of each dice roll with a random number between 1 and 6
            dice_roll = random.randint(dice_lowest_value, dice_highest_value)
            # Adds dice roll result to the total number of results
            dice_total += dice_roll
        # Counts how many times a particular dice total is rolled
        dice_counter[dice_total] += 1


def calc_and_output_empirical_results():
    # Creates a global array to hold each resultant's ratio to the total number of trials
    global empirical_ratios
    empirical_ratios = stdarray.create1D(dice_highest_result, 0)

    stdio.writeln('Empirical results')
    # This loop will calculate each resultant's ratio to total trials
    for num in range(dice_lowest_result, dice_highest_result):
        # Adds num's 'ratio to total trials' to empirical_ratios array
        empirical_ratios[num] = dice_counter[num] / num_trials
        stdio.writeln(f"Results the sum of die is {num}: {empirical_ratios[num]}")
    # Makes the code look cleaner in command line
    stdio.writeln("")


def output_exact_probabilities():
    # this loop will write out the exact probabilities rounded to the nearest 4th decimal.
    stdio.writeln("Exact Results")
    for num in range(dice_lowest_result, dice_highest_result):
        stdio.writeln(f"Probability the sum of die is {num}: {round(probabilities[num], 4)}")
    stdio.writeln("")


def calc_and_output_differential_results():
    # this loop will write out the difference between the exact probability and empirical results.
    # Also rounded to the nearest 4th decimal. I chose to do this because I think it looks cleaner.
    stdio.writeln("Difference")
    for num in range(dice_lowest_result, dice_highest_result):
        stdio.writeln(f"Difference when sum is {num}: {round(probabilities[num] - empirical_ratios[num], 4)}")


# Main function that ties all the other functions together and allows the program to run.
def main():
    # Takes any integer input by the user to be the number of dice roll trials
    global num_trials
    num_trials = int(sys.argv[1])

    # Style preference at the beginning and end for readability
    stdio.writeln("")

    probability_formula()

    output_exact_probabilities()

    run_dice_trials()

    calc_and_output_empirical_results()

    calc_and_output_differential_results()

    stdio.writeln("")


# Runs program
if __name__ == '__main__':
    main()

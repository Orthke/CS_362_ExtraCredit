# Write a program that takes an array of integers - array and an integer target_sum.
# Your program should return an array containing two numbers that add up to the target... 


def find_sum_combibation(numbers, target):
    
    for num in numbers:
        for rest in numbers:
            if num + rest == target:
                return [num, rest]

    return None


if __name__ == "__main__":
    print(find_sum_combibation([2,7,11,15], 9))

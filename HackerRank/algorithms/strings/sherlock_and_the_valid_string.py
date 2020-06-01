# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Sherlock and the Valid String
# problem url: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# date: 05/30/2020

def create_freq_list(string):
    frequencies = {}
    for letter in string:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return list(frequencies.values())


def is_valid_string(freq_lst):
    freq_max = max(freq_lst)
    freq_min = min(freq_lst)
    max_count = freq_lst.count(freq_max)
    min_count = freq_lst.count(freq_min)

    if freq_min == freq_max:
        return True
    elif max_count + min_count == len(freq_lst):
        if freq_min == 1 and min_count == 1:
            return True
        elif  (freq_max - 1) == freq_min and max_count == 1:
            return True
        else:
            return False
    else:
        return False


def main():
    input_str = input()
    freq_lst = create_freq_list(input_str)
    print("YES" if is_valid_string(freq_lst) else "NO")

main()

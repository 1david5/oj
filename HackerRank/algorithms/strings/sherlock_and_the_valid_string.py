# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Sherlock and the Valid String
# problem url: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# date: 05/30/2020

def equal_freq(iterator):
    if iterator.count(iterator[0]) == len(iterator):
        return True
    else:
        return False

input_str = input()
frequencies = {}
for letter in input_str:
    if letter in frequencies:
        frequencies[letter] += 1
    else:
        frequencies[letter] = 1

freq_lst = list(frequencies.values())

if equal_freq(freq_lst):
    print("YES")
else:
    out_of_freq = 0
    for i in range(len(freq_lst) - 1):
        if freq_lst[i + 1] == freq_lst[i]:
            continue
        elif freq_lst[i + 1] == 1:
            del freq_lst[i + 1]
            if equal_freq(freq_lst):
                print("YES")
                exit()
            else:
                print("NO")
                exit()
        elif (freq_lst[i + 1] - 1) == freq_lst[i]:
            out_of_freq += 1
            freq_lst[i + 1] -= 1
        else:
            print("NO")
            exit()
        if out_of_freq > 1:
            print("NO")
            exit()
    print("YES")

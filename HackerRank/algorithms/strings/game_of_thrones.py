# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Game of Thrones - I
# problem url: https://www.hackerrank.com/challenges/game-of-thrones/problem
# date: 06/03/2020

def list_of_frequencies(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return list(char_freq.values())

def game_of_thrones(s):
    freq_list = list_of_frequencies(s)
    odd_count = 0
    for freq in freq_list:
        if freq % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return "NO"
    return "YES"

print(game_of_thrones(input()))
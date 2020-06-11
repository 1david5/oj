# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Migratory Birds
# problem url: https://www.hackerrank.com/challenges/migratory-birds/problem
# date: 06/11/2020

def frequency_dictionary(l):
    dic = {}
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

def migratory_birds(n, lst):
    freq_d = frequency_dictionary(lst)
    max_freq = max(freq_d.values())
    popular_bird = list(freq_d.keys())[list(freq_d.values()).index(max_freq)]
    for bird, freq in freq_d.items():
        if freq == max_freq and bird < popular_bird:
            popular_bird = bird
    return popular_bird

def main():
    sights_cnt = int(input())
    sights_lst = list(map(int, input().strip().split()))
    print(migratory_birds(sights_cnt, sights_lst))

if __name__ == "__main__":
    main()
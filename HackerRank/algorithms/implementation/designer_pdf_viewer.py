# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Designer PDF Viewer
# problem url: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# date: 06/25/2020

if __name__ == "__main__":
    heights = [int(i) for i in input().strip().split()]
    word = input()
    print(len(word) * max(heights[ord(letter) - ord('a')] for letter in word))
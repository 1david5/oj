# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Time Conversion
# problem url: https://www.hackerrank.com/challenges/time-conversion/problem
# date: 06/02/2019

def timeConversion(time):
    z = '00'
    h = int(time[:2]) + 12
    if time[-2] == 'A':
        if h == 24:
            return z + time[2:8]
        return time[:8]      
    else:
        if h !=24:
            return str(h) + time[2:8]
        return time[:8]
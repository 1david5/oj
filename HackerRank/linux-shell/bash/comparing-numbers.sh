# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Linux Shell: Bash: Comparing Numbers
# problem url: https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problemproblem
# date: 05/18/2020

#!/bin/bash
read X
read Y

if [ $X -gt $Y ]
then
    echo "X is greater than Y"
elif [ $X -lt $Y ]
then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi
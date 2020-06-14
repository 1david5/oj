# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Bon Appétit
# problem url: https://www.hackerrank.com/challenges/bon-appetit/problem
# date: 06/14/2020

def bon_appetit(alergic_index, bill, charge):
    right_charge = (sum(bill) - bill[alergic_index]) // 2
    return "Bon Appetit" if charge == right_charge else abs(charge - right_charge)

def main():
    nk = input().strip().split()

    items_count = int(nk[0])
    alergic_index = int(nk[1])
    bill = list(map(int, input().strip().split()))
    charge = int(input())

    print(bon_appetit(alergic_index, bill, charge))

if __name__ == "__main__":
    main()

# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Electronics Shop
# problem url: https://www.hackerrank.com/challenges/electronics-shop/problem
# date: 06/17/2020

def get_money_spent(budget, keyboard, usb):
    spent = -1
    for k in keyboard:
        for u in usb:
            purchase = k + u
            if spent < purchase <= budget:
                spent = purchase
    return spent

def main():
    b_n_m = input().strip().split()
    budget = int(b_n_m[0])
    keboard_count = int(b_n_m[1])
    usb_count = int(b_n_m[2])
    keyboards_price = list(map(int, input().strip().split()))
    usb_price = list(map(int, input().strip().split()))
    print(get_money_spent(budget, keyboards_price, usb_price))

if __name__ == "__main__":
    main()
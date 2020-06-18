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
    budget, k_count, u_count = [int(i) for i in input().strip().split()]
    keyboards_price = [int(k) for k in input().strip().split()]
    usb_price = [int(u) for u in input().strip().split()]
    print(get_money_spent(budget, keyboards_price, usb_price))

if __name__ == "__main__":
    main()
def get_total(price, tip):
    # 'return' sends the answer back so we can use it later
    return price + (price * 0.08) + (price * (tip / 100))

# Usage
bill = 100
tip_pct = 20

final_amount = get_total(bill, tip_pct)
print("Total Due:", final_amount)
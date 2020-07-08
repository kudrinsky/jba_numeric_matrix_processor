def final_deposit_amount(*interest, amount=1000):
    for month in interest:
        amount *= 1 + month / 100
    return round(amount, 2)
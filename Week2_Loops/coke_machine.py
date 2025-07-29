print("Amount Due: 50")
total = 50
while True:
    prompt = int(input("Insert Coin: "))
    if prompt ==5 or prompt == 10 or prompt == 25:
        total = total - prompt
        if total > 0:
            print(f"Amount Due: {total}")
            continue
        elif total <= 0:
            total = abs(total)
            print(f"Change Owed: {total}")
            break
    else:
        print(f"Amount Due: {total}")
        continue
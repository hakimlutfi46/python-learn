data_toko = {
    "Indomaret": {
        "Ayam": 30000,
        "Sayur": 15000,
        "Buah": 20000,
        "Ikan": 22000
    },
    "Alfamaret": {
        "Ayam": 25000,
        "Sayur": 12000,
        "Buah": 30000,
        "Ikan": 25000
    },
}

item_to_buy = {
    "Ayam": 2,
    "Sayur": 1,
    "Ikan": 1
}

total_cost = 0

print("Rincian Pembelian:")
for item, quantity in item_to_buy.items():
    price_per_item = data_toko["Indomaret"][item]
    subtotal = price_per_item * quantity
    print(f"{item}: {quantity} * {price_per_item} = {subtotal}")
    total_cost += subtotal

print("\nTotal Biaya: ", total_cost)
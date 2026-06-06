from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 15", "+79001234567"),
    Smartphone("Samsung", "Galaxy S24", "+79007654321"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79003334455"),
    Smartphone("Google", "Pixel 8", "+79009998877"),
    Smartphone("Huawei", "P60 Pro", "+79006667788"),
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")

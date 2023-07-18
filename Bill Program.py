from tabulate import tabulate
from PIL import Image, ImageDraw, ImageFont

def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item['amount'] * item['quantity']
    return subtotal

def calculate_total(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return total

def generate_bill_table(items, tax_rate):
    headers = ['Item', 'Quantity', 'Amount']
    rows = []
    for item in items:
        row = [item['name'], item['quantity'], item['amount']]
        rows.append(row)

    subtotal = calculate_subtotal(items)
    tax_amount = subtotal * tax_rate
    total = calculate_total(subtotal, tax_rate)

    footer = [['Subtotal', '', subtotal],
              ['Tax', '', tax_amount],
              ['Total', '', total]]

    table = tabulate(rows, headers, tablefmt='grid')
    table += '\n' + tabulate(footer, tablefmt='grid')

    return table

# Get user input
print("")
print("**********Welcome To Supermarket**********")
print("")
items = []
while True:
    name = input("Enter Item Name(Type 'done' To Finish): ")
    if name == 'done':
        break
    quantity = int(input("Enter Quantity Of The Item: "))
    amount = float(input("Enter Amount Of The Item: "))
    print()

    item = {'name': name, 'quantity': quantity, 'amount': amount}
    items.append(item)

tax_rate = 0.05  # 5% tax rate

bill_table = generate_bill_table(items, tax_rate)
table_image = Image.new('RGB', (400, 800), color=(255, 255, 255))
draw = ImageDraw.Draw(table_image)
font = ImageFont.load_default()
draw.text((10, 10), bill_table, font=font, fill=(0, 0, 0))
table_image.save('Bill.png')
print("")
print(bill_table);
print("")
print("Bill Table Saved As 'Bill.png'")
print("")

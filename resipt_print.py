import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def get_user_inputs():
    customer_name = input("Enter Customer Name: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    items = []
    while True:
        item_name = input("Enter Item Name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_amount = float(input(f"Enter amount for {item_name}: "))
        items.append((item_name, item_amount))

    return customer_name, date, items

def generate_receipt_number():
    return str(random.randint(100000, 999999))

def create_receipt(receipt_number, date, company_name, items, total_amount, customer_name, filename="receipt.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Draw the header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "Payment Receipt")

    # Draw the receipt details
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Receipt Number: {receipt_number}")
    c.drawString(50, height - 120, f"Date: {date}")
    c.drawString(50, height - 140, f"Company Name: {company_name}")

    # Draw the customer details
    c.drawString(50, height - 180, f"Customer Name: {customer_name}")

    # Draw the items table
    c.drawString(50, height - 220, "Items:")
    c.drawString(50, height - 240, "Description")
    c.drawString(300, height - 240, "Amount")

    y = height - 260
    for item, amount in items:
        c.drawString(50, y, item)
        c.drawString(300, y, f"${amount:.2f}")
        y -= 20

    # Draw the total amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Total Amount: ${total_amount:.2f}")

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(50, 50, "Thank you for your business!")

    c.showPage()
    c.save()

def main():
    company_name = "Awesome Company"
    
    customer_name, date, items = get_user_inputs()
    total_amount = sum(amount for item, amount in items)
    receipt_number = generate_receipt_number()

    create_receipt(receipt_number, date, company_name, items, total_amount, customer_name, "payment_receipt.pdf")
    print("Receipt created successfully as 'payment_receipt.pdf'.")

if __name__ == "__main__":
    main()

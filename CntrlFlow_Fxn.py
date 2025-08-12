# Function calculates final price after applying a discount

def calculate_discount(price, discount_percent):
    """Calculate the final price after applying the discount if >= 20%."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example usage:
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")
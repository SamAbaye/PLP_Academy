#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

price = input("Please input the price of the item: ")
discount_percent = input("Please input the discount percentage: ")

final_price = calculate_discount(float(price), float(discount_percent))
print("The final price is: ", final_price)

#lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. \n"

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. \n"

stylish_settee_price= 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. \n"

luxurious_lamp_price = 52.15

sales_tax = "8.8%"

sale_total = 0


# Test print for variables
#print(lovely_loveseat_description, lovely_loveseat_price, stylish_settee_description,stylish_settee_price,luxurious_lamp_description,luxurious_lamp_price,sales_tax)

#############################

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_final = customer_one_total * 1.088

print("Customer One Items: \n")
print(customer_one_itemization)
print("            Sub Total: " + str(customer_one_total))
print("            Sales Tax: " + sales_tax)
print("   Customer One Total: " + str(customer_one_final))

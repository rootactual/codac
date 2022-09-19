flat = 20.0
weight = 41.5

cost_g = 0
cost_p = 125.00
cost_d = 0

#Ground Shipping
if weight <= 2:
  cost_g = weight * 1.5 + flat
elif weight > 2 and weight <= 6:
  cost_g = weight * 3.0 + flat
elif weight > 6 and weight <= 10:
  cost_g = 4.0 * weight + flat
else:
  cost_g = 4.75 * weight + flat

# Test Calc Ground Print
print(cost_g)

#Premium Shipping
print(cost_p)

#Drone Shipping
if weight <= 2:
  cost_d = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_d = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_d = weight * 12.00
else:
  cost_d = weight * 14.25

print(cost_d)

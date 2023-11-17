""" 
Build a meter system for an auto. Take into two inputs. Kilometers Travelled and Stall Time (in minutes). Rate List -
First 10 kms - Rs 10 per Km
Next 40 kms - Rs 9 per Km
Next 100 kms - Rs 8 per Km
Any leftover km count - Rs. 6 per Km
Rs 5 extra for every minute of Stall Time.
 """

km = float(input("Enter km: "))
time = float(input("Enter time in minute: "))
total_price = 0
if km <= 10:
    total_price = km * 10
elif km > 10 and km <= 50:
    total_price = (10 * 10) + (km - 10) * 9
elif km > 50 and km <= 150:
    total_price = (10 * 10) + (40 * 9) + (km - 50) * 8
else:
    total_price = (10 * 10) + (40 * 9) + (100 * 8) + (km-150) * 6

total_price += (time * 5)

print(total_price)

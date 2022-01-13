# this program stores and print messages regarding motorcycles manufactures

motorcycles_brands = ['Honda','Suzuki','Yamaha','Triumph','Royal Enfield','Harley Davidson']

print(f"\tThe {motorcycles_brands[0].title()} is likely to be the most famous in Brazil")

the_desired_motorcycle = f"i wish I have money to buy a {motorcycles_brands[-1].title()} for riding on the weekends"
print(f"\n\n{the_desired_motorcycle.title()}")

motorcycles = []
motorcycles.append('low rider')
motorcycles.append('shadow')
motorcycles.append('iron883')
motorcycles.insert(1,'fat boy')

wished_motorcycles = motorcycles.pop()

print(f"\n\n{motorcycles}")
print(f"\n\n{wished_motorcycles}")
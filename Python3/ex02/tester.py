from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

# Jaine = Joffrey.create_lannister("Jaine", True)
# print(f"Name : {Jaine.first_name, type(Jaine).__name__},", end="")
# print(f" Alive : {Jaine.is_alive}")

from S1E9 import Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

print("---")
Lyanna.change_health_state()
print(Lyanna.is_alive)
Lyanna.change_health_state()
print(Lyanna.is_alive)
Lyanna.change_health_state()
print(Lyanna.is_alive)

# from S1E9 import Character

# try:
#     hodor = Character("hodor")
# except Exception as err:
#     print(err)

waiting_list = ['sen', 'koji', 'bello', 'phil']
waiting_list.sort()

for index, item in enumerate(waiting_list, 1):
    print(f"{index}.: {item.title()}")

filenames = ['document','report', 'presentation']

for k,v in enumerate(filenames):
    print(f"{k}-{v.title()}.txt")

"""Coding Exercise 2.
1. Promps the user to input an index(e.g 0 or 1)
2. Returns the IP address that has index 
"""
ips = ['100.122.1333.105','100.122.133.111']

user_prompt = int(input('Enter the index of the IP you want: '))

for k,v in enumerate(ips):
    if k == user_prompt:
        print(f"You chose {v}")


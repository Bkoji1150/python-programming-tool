ips = ['100.122.133.105', '100.122.133.111']
user_prompt = int(input("Enter the index of the IP you want: "))

for i,v in enumerate(ips):
    if user_prompt == i:
        print(f"You chose {v}")
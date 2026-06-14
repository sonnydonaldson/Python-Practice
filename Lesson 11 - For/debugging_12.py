banned_items = ["slingshot","laser"]
inventory = ["apple","slingshot","book","laser"]
confiscated = []
print(f"Scanning inventory: {inventory}")
for item in inventory:
    if item in banned_items:
        print(f"Alert! Found banned item: {item}")
        confiscated.append(item)
        inventory.remove(item)
        print(f"Scan complete. Total flag matches: {len(banned_items)}")
if len(confiscated) > 0:
    print("Items confiscated:")
    for item in range(len(confiscated)):
        print(f'{item+1}.{confiscated[item]}')
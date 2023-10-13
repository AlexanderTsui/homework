people = list(range(1, 224))
index = 0

while len(people) > 1:
    index = (index + 2) % len(people)
    removed_person = people.pop(index)
    print(f"第{removed_person}号退出圈子")

print(f"最后留下的是原来第{people[0]}号的那位")

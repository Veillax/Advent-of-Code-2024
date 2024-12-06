def check_update_order(update, rules):
  for rule in rules:
    page1, page2 = rule
    if page1 in update and page2 in update:
      if update.index(page1) > update.index(page2):
        return False
  return True
with open("input.txt", "r", encoding="utf-8") as f:
    content = f.read()
section_split = "\n\n"
sections = content.split(section_split)
unparsed_rules = sections[0].strip()
unparsed_updates = sections[1].strip()
rules = []
updates = []
result = 0
for rule in unparsed_rules.split("\n"):
    if rule.strip():
        x, y = rule.split("|")
        rules.append((int(x.strip()), int(y.strip())))
for update in unparsed_updates.split("\n"):
    if update.strip():
        updates.append([int(x.strip()) for x in update.split(",")])
for update in updates:
  if check_update_order(update, rules):
    middle_index = len(update) // 2
    middle_page = update[middle_index]
    print(f"Correctly ordered update: {update}, Middle page: {middle_page}")
    result += middle_page  
print(result)
def reorder_update(update, rules):
  ordered_update = []
  remaining_pages = update.copy()
  while remaining_pages:
    for page in remaining_pages:
      can_add = True
      for rule in rules:
        if rule[0] == page and rule[1] in remaining_pages:
          can_add = False
          break
      if can_add:
        ordered_update.append(page)
        remaining_pages.remove(page)
        break
  return ordered_update
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
incorrectly_ordered_updates = []
result = 0  # For correctly ordered updates
for update in updates:
  if check_update_order(update, rules):
    middle_index = len(update) // 2
    middle_page = update[middle_index]
    print(f"Correctly ordered update: {update}, Middle page: {middle_page}")
    result += middle_page
  else:
    incorrectly_ordered_updates.append(update)
print(f"Sum of middle page numbers of correctly-ordered updates: {result}")
reordered_updates = [reorder_update(update, rules) for update in incorrectly_ordered_updates]
middle_page_sum = 0
for update in reordered_updates:
  middle_index = len(update) // 2
  middle_page = update[middle_index]
  middle_page_sum += middle_page
print(f"Sum of middle page numbers of incorrectly-ordered updates: {middle_page_sum}")

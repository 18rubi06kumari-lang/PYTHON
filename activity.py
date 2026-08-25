total_chores = 4
original_count = total_chores

print(f"you have{original_count}task finish today \n")

complete_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "make bed"
    elif chore_num == 2: next_chore = "feed the pet"
    elif chore_num == 3: next_chore = "take out trash"
    else: next_chore == "wash dishes"

    answer = input(f"have you fineshed chores{next_chore}? (yes/no)")

    if answer == "yes":
        complete_count += 1
        chore_num += 1
        print("good job")
    else: 
        print("finish it and check again")


    print("chores remainig:",total_chores - complete_count)
    print()


print("=====ALL CHORES DONE=====")
print("great work finishing your entire chores checklist today \n")

print("===: smart school day planner ===")
print("answer 3 quick question and i will plan your day \n")

day  = input("what day is it ? (monday-sunday): ").strip().capitalize()
weather  = input("what is the weather ? (sunny/rainy/cloudy): ").strip().lower()
homework  = input("is your homework done  ? (yes/no): ").strip().lower()

if day in ("saturday","sunday")
 print("day type  : weekend-enjoy your free time!")

elif day =="monday":
 print("day type  : first day of week.pack weekly planner !")

elif day =="friday":
 print("day type  : last day of week.pack your libray books !")

elif day in "tuesday","wednesday","friday":
 print("day type  : regular school.stay focused !")

else:
 print("day type  : day cannot be recognized. please check your spelling !")

if weather == "sunny" and homework == "yes":
 print(" after school: head to park-great weather and homework is done")

if weather == "rainy" or weather == "cloudy":
  print(" weather tip: pack your umbrella it may get wet")




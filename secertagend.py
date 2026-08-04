#part1 ask agent for their details
name=input("enter you real name, agent:" )
gadget=input("enter you favorite gadget:" )

#part2 store the agent details using differenr data types
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.87
is_active = True

#part3 print detail along with datstypes

print("name:",name, "type", type(name))
print("gadget:",gadget, "type", type(gadget))
print("agent number:",agent_number, "type", type(agent_number))
print("speed rating:",speed_rating, "type", type(speed_rating))
print("misson count:",mission_count, "type", type(mission_count))
print("height(m):",height_m,"type", type(height_m))
print("is active :" ,is_active ,"type", type(is_active))

#part4 typecast on number true and false value inti text

agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(status)

print("agent number as text",agent_number_text, "type", type(agent_number_text))
print("speed rating as text",speed_rating_text, "type", type(speed_rating_text))
print("mission count as text",mission_count_text, "type", type(mission_count_text))
print("status as text",status_text, "type", type(status_text))


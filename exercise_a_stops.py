stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print('question_1')
print(stops)

#2. Add "Glasgow Queen St" to the start of the list
print('question_2')
stops.insert(0, "Glasgow Queen St")
print(stops)

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
print('question_3')
stops.insert(4, "Polmont")
print(stops)

#4. Print out the index position of "Linlithgow"
print('question_4')
print(stops.index("Linlithgow"))

#5. Remove "Livingston" from the list using its name
print('question_5')
stops.remove("Livingston")
print(stops)

#6. Delete "Cumbernauld" from the list by index
print('question_6')
stops.pop(2)
print(stops)

#7. Print the number of stops there are in the list
print('question_7')
print (len(stops))

#8. Sort the list alphabetically
print('question_8')
stops.sort()
print(stops)

#9. Reverse the positions of the stops in the list
print('question_9')
stops.reverse()
print(stops)

#10 Print out all the stops using a for loop
print('question_10')
for stop in stops:
    print(stop)

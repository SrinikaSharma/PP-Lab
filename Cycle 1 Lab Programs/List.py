myList = ["BVRIT", "HYDERABAD", "College", "of", "Engineering", "for", "Women"]
print(myList)
print(myList[0])
print(myList[4]) 
print(myList[-1]) 
myList.append(["CSE", "AIML"])
print(myList)
len(myList)
myList.remove("for")
print(myList)
myList.remove("Women")
print(myList)
myList.remove(["CSE", "AIML"])
print(myList)
myList.pop()
print(myList)

'''Output
['BVRIT', 'HYDERABAD', 'College', 'of', 'Engineering', 'for', 'Women']
BVRIT
Engineering
Women
['BVRIT', 'HYDERABAD', 'College', 'of', 'Engineering', 'for', 'Women', ['CSE', 'AIML']]
['BVRIT', 'HYDERABAD', 'College', 'of', 'Engineering', 'Women', ['CSE', 'AIML']]
['BVRIT', 'HYDERABAD', 'College', 'of', 'Engineering', ['CSE', 'AIML']]
['BVRIT', 'HYDERABAD', 'College', 'of', 'Engineering']
['BVRIT', 'HYDERABAD', 'College', 'of']
'''

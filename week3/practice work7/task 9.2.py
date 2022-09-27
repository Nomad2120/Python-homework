import statistics

def product_of_elements(myList):

	result = 1
	for x in myList:
		result = result * x
	return result


list = [[17, 13, 32],[7, 2, 9],[21, 27, 5]]

for i in range(3):
    print("Your product of the elements in",i+1," list =", product_of_elements(list[i]))

for i in range(3):
    print("Your arithmetic mean of ",i+1,"list =", statistics.mean(list[i]))
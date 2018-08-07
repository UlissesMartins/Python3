number = [7,8,9,15,1,2,7,8,9,7]

def remove_repetidos(list):

	remove = []

	list.sort()

	for x in range(0,len(list)-1):

		if not (list[x] == list[x+1]):
			remove.append(list[x])

	remove.append(list[len(list)-1])

	return remove
number = remove_repetidos(number)
print(number[:len(number)])

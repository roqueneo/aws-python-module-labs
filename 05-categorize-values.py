# Mixed type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("Value {} is of the data type {}".format(item,type(item)))
    
print('\n')
    
for item in range(2, 20, 2):
    print("Value {} is of the data type {}".format(item,type(item)))
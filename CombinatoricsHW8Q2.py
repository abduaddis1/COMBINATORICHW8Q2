def getNumShuffles(initialDeck):
    list1 = initialDeck[:len(initialDeck)//2]
    list2 = initialDeck[len(initialDeck)//2:]
    
    # print(firstHalf)
    # print(secondHalf)
    counter =  0
    list3 = []
    while(not list3 == initialDeck):
        list3=[]
        while True:
            try:
                list3.append(list1.pop(0))
                list3.append(list2.pop(0))
            except IndexError:
                break
        list1 = list3[:len(list3)//2]
        list2 = list3[len(list3)//2:]
        counter += 1
        # print(list3)
    
    # print(counter)
    return counter


for i in range(2,41,2):
    testList = [x for x in range(i)]
    count = getNumShuffles(testList)
    # check = 2 % (2*i//2 + 1)
    print("Num shuffles for : ", i//2, count)
        




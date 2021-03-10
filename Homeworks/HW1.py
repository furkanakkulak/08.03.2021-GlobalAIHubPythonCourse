List1 = [1,3,5,7,9]
List2 = [2,4,6,8]
MergedList = List1 + List2
print("Merged List: ", MergedList)
MergedList.sort()
print("Sort Merged List: ", MergedList)
for i in range (len(MergedList)):
    MergedList[i]*=2
print("Merged List * 2: ", MergedList)
print("Veri Tipi: ",type(MergedList))
for i in MergedList:
  print("Data type of the",i//2,"element",type(i))

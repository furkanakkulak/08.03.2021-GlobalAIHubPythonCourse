List1 = [1,3,5,7,9]
List2 = [2,4,6,8]
MergeList = List1 + List2
print("Merge List: ", MergeList)
MergeList.sort()
print("Sort Merge List: ", MergeList)
for i in range (len(MergeList)):
    MergeList[i]*=2
print("Merge List * 2: ", MergeList)
print("Type: ",type(MergeList))

#
# masterDict = []
#
# for i in range(999):
#     whatToDo = input("Add or Done?")
#     if whatToDo == "Done":
#         break
#     else:
#         personName = input("Enter Name:")
#         personAge = input("Enter Age:")
#         personHometown = input("Enter Hometown:")
#         masterDict.append([personName, personAge, personHometown])
#
# masterDict = sorted(masterDict, key=lambda dct: dct[1])
#
# print("Name\tAge\tHometown")
# print("------------------------")
# stringStuff = "{}\t{}\t{}"
#
# for item in masterDict:
#     print(stringStuff.format(item[0], item[1], item[2]))

# arrayOfNums = [3,1,77,3,8,4,12,78,97,123,56,38]
# finalArray = []
#
# finalArray.append(arrayOfNums[0])
#
# for number in arrayOfNums:
#     for comparNum in range(len(finalArray)):
#         if finalArray[comparNum] >= number:
#             finalArray.insert(comparNum, number)
#
#
# print(finalArray)
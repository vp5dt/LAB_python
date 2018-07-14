values=input("Enter the list of numbers seperated by space: ")
values= values.split(" ")
if values[(len(values)-1)]=='':
    values.remove('')
print("Given List:")
print(values)


def findtriplets(arr, n):
    flag = True

    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):


                if (int(arr[i]) + int(arr[j]) + int(arr[k]) == 0):
                    tup=(int(arr[i]),int(arr[j]),int(arr[k]))

                    print(tup)
                    flag = True
    if flag==False:
        print("No Such Triplet exist")

findtriplets(values,len(values))
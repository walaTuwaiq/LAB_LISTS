# Q1:
lst = [2,5,11,3.6]
sumItems=0

for num in lst:
    sumItems+=num

print(sumItems," Is sum items")


# Q2:
largestNum = lst[0]

for index in range(len(lst)):
    if index > 0:
        if lst[index] > lst[index-1]:
            largestNum = lst[index]
        else:
            largestNum = lst[index-1]

print(largestNum," Is largest number in a list.")

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

oddNumbers = [ oddNum for oddNum in range(1200,2000,125) if not oddNum % 2 == 0  ]
print(oddNumbers, " Is list to odd numbers between 1200 to 2000 with step 125.")
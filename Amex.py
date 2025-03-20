#WithsimplifiedSolution
#numbers=[1,2,3,4,5,6,7,8,9,0]
#output=[]
#
#for i in range(0,len(numbers),3):
#    output.append(numbers[i:i+3])
#
#print(output)

#WithoutSimplification
numbers=[1,2,3,4,5,6,7,8,9,0]
OutList1=[]
OutList2=[]
cnt=0

for i in numbers:
    if cnt<3:
        OutList1.append(i)
        cnt+=1
    elif cnt==3:
        OutList2.append(OutList1[0:3])
        OutList1.clear()
        OutList1.append(i)
        cnt=1

if OutList1:
    OutList2.append(OutList1[:])

print(OutList2)


class solution:
    def row_sum(self,array,row):
        n=len(array[0])
        b=[]
        for i in range (row):
            sum=0
            for j in range (n):
                sum+=array[i][j]
            b.append(sum)
        return b
a1=solution()
arr=[]
row =int(input())
for i in range (row):
    column=list(map(int,input().split()))
    arr.append(column)
print(a1.row_sum(arr,row))

import csv

inputpath=input("Enter the input path file:")
countWhat=input("Enter what needs to be count:")

count=0
'''Without using any data structure
inputfile =open(inputpath,'r')
print("Successfully read csv file!!!")
count=0
for i in inputfile:
    if countWhat in i:
        count+=1 works for alteast one occurance

print("The occurance of "+countWhat+" in th file is "+str(count))'''

'''Using list to count specific word'''
with open(inputpath,'r',newline='') as inputfile:
    csv_reader = csv.reader(inputfile,delimiter=' ')
    for i in csv_reader:
        for j in i:
            if (countWhat in j):
                count+=1

print("The occurance of "+countWhat+" in th file is "+str(count))

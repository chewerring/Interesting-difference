#Read the files
inputfile = open("difin.txt", "r")
outputfile = open("difout.txt", "w")

#Get the value as an integer
value = inputfile.read().split()
value = int(value[0])

#Write the function that calculates
def dif(n):
    if n > 17:
        answer = n - 17
        answer *= 2
    else:
        answer = 17 - n
    return answer
        
#Run the function
answer = dif(value)

#Output the answer
outputfile.write(str(answer))

#Close the files
inputfile.close()
outputfile.close()

file = open('uSR.txt')
file1 = open('pWD.txt')
line= file.readline()
lines= file1.readline()
while line!="":
    print(line)
    print(lines)
    line= file.readline()
    lines= file1.readline()
file.close   




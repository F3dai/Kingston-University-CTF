import sys
if not len(sys.argv) == 2:
    print("Syntax: rev2.py <flag>")
    exit()

input = sys.argv[1]
password = ""
intPass = '''
    0x6d, 0x73, 0x65, 0x75, 0x75, 
    0x7d, 0x4b, 0x49, 0x48, 0x6d, 
    0x35, 0x7f, 0x59, 0x65, 0x36, 
    0x62, 0x63, 0x7b
'''
intPass = intPass.split(",")
flagCounter = 0
for i in range(len(intPass)):
        value = chr(int(intPass[i], 0) ^ 0x6)
        if(input[i] == value):
            flagCounter += 1
        else:
            print("hmm..think harder.")
if(flagCounter == 98):
	print(value)

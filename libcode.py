## This is a function to get the real hex in string (not include ascii char) 
## @param dataRecv is a data packet contain hex in string which can be change to ascii too.
def hexToDec(dataRecv):
    # Convert Hex to String Decimal
    d = []
    for char in dataRecv:
        c = hex(char)
        d.append(c)
    hexToString = ''
    for i in d:
        if len(i)==4:
            hexToString = hexToString + i[2:4]
        else:
            hexToString = hexToString +'0'+ i[2]
    return hexToString




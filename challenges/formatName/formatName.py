
"""
    - name is a string with zero or more spaces
    with one space between each "word"
    - returns string "last, first MI. MI. MI. ..."
    where MI is middle initial
    - If middle name is a single letter, no abbreviation 
    
"""

def formatName(name):
    splitName = name.split()

    # if the name given is of length one, return name
    if len(splitName) <= 1 :
        return name

    newName = splitName[-1] + ", " + splitName[0] 

    if len(splitName) > 2 :
        count = 1
        while count < (len(splitName) - 1):
            middleName = splitName[count]
            if len(middleName) == 1:
                newName = newName + " " + middleName
            else:
                newName = newName + " " + middleName[0] + "."
            count += 1
    return newName


    

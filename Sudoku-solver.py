import math
import re
#Hw 6 - Sudoku solver using CSP and Backtracking
#Cole Robinson and Joel Hilliard

#Gameboard 1.
# ___________________
#| 0 0 1|0 0 2|0 0 0 |
#| 0 0 5|0 0 6|0 3 0 |
#| 4 6 0|0 0 5|0 0 0 |
#|-------------------|
#| 0 0 0|1 0 4|0 0 0 |
#| 6 0 0|8 0 0|1 4 3 |
#| 0 0 0|0 9 0|5 0 8 |
#|-------------------|
#| 8 0 0|0 4 9|0 5 0 |
#| 1 0 0|3 2 0|0 0 0 |
#| 0 0 9|0 0 0|3 0 0 |
# -------------------

#Size of game board is 9x9 so 81 squares total indexd 0-80.
gameBoard1 = [
  0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 0, 6, 0, 3, 0, 4, 6, 0, 0, 0, 5, 0, 0,
  0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 6, 0, 0, 8, 0, 0, 1, 4, 3, 0, 0, 0, 0, 9, 0, 5,
  0, 8, 0, 0, 0, 0, 4, 9, 0, 5, 0, 1, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0,
  3, 0, 0
]


#Gameboard 2.
# ___________________
#| 0 0 5|0 1 0|0 0 0 |
#| 0 0 2|0 0 4|0 3 0 |
#| 1 0 9|0 0 0|2 0 6 |
#|-------------------|
#| 2 0 0|0 3 4|0 0 0 |
#| 0 4 0|0 0 0|7 0 0 |
#| 5 0 0|0 0 7|0 0 1 |
#|-------------------|
#| 0 0 0|6 0 3|0 0 0 |
#| 0 6 0|1 0 0|0 0 0 |
#| 0 0 0|0 7 0|0 5 0 |
# -------------------

#Size of game board is 9x9 so 81 squares total indexd 0-80.
gameBoard2 = [
              0,0,5,0,1,0,0,0,0,
              0,0,2,0,0,4,0,3,0,
              1,0,9,0,0,0,2,0,6,
              2,0,0,0,3,0,0,0,0,
              0,4,0,0,0,0,7,0,0,
              5,0,0,0,0,7,0,0,1,
              0,0,0,6,0,3,0,0,0,
              0,6,0,1,0,0,0,0,0,
              0,0,0,0,7,0,0,5,0
]


#Gameboard 3.
# ___________________
#| 0 0 1|0 0 2|0 0 0 |
#| 0 0 5|0 0 6|0 3 0 |
#| 4 6 0|0 0 5|0 0 0 |
#|-------------------|
#| 0 0 0|1 0 4|0 0 0 |
#| 6 0 0|8 0 0|1 4 3 |
#| 0 0 0|0 9 0|5 0 8 |
#|-------------------|
#| 8 0 0|0 4 9|0 5 0 |
#| 1 0 0|3 2 0|0 0 0 |
#| 0 0 9|0 0 0|3 0 0 |
# -------------------





gameBoard2 = [0,0,5,0,1,0,0,0,0,
              0,0,2,0,0,4,0,3,0,
              1,0,9,0,0,0,2,0,6,
              2,0,0,0,3,0,0,0,0,
              0,4,0,0,0,0,7,0,0,
              5,0,0,0,0,7,0,0,1,
              0,0,0,6,0,3,0,0,0,
              0,6,0,1,0,0,0,0,0,
              0,0,0,0,7,0,0,5,0]


#This function will take the current game board and return a list of column lists. ex. colList[0] = [0,0,4,0,6,0,8,1,0]
#into a list
def createListofColumns(gameBoard):

  #This is the outer list of column lists
  colList = []

  for i in range(0, 9):

    #This is a list containg the values of each column
    columns = []

    for j in range(0, 9):
      #print("j: " + str(j) + " i: " + str(i))
      #print(gameBoard[(j*9)+i])
      columns.append(gameBoard[(j * 9) + i])

    colList.append(columns)
    #print("columns[] = " + str(columns))

  #print("colList[] = " + str(colList))

  return colList


#This function will take the current game board and return a list of row lists.
# ex. rowList[0] = [0,0,1,0,0,2,0,0,0]
def createListofRows(gameBoard):
  rowList = []

  for i in range(0, 9):

    rows = []

    for j in range(0, 9):

      rows.append(gameBoard[(i * 9) + j])

    rowList.append(rows)

    #print("rows[] = " + str(rows))
  #print("\nrowList[] = " + str(rowList))

  return rowList


#This function will use the list of rows we have already created and take the elements from
#from each row in sets of 3 and put them in a square list
def createListofSquares(rowList):

  squareList = []

  for l in range(0, 3):

    for i in range(0, 3):
      #Reset the contents of current square
      squares = []

      for j in range(0, 3):

        for k in range(0, 3):

          #This gets all of the squares in order. Now just need to append them in proper spots.
          #print("i = " + str(i) + "Rowlist[" + str(j+(l*3)) + "][" + str(k+(i*3)) + "] = " + str(rowList[j+(l*3)][k+(i*3)]))
          squares.append(rowList[j + (l * 3)][k + (i * 3)])

        #print("End of k")
      squareList.append(squares)
      #print("End of j")

    #print("End of i")
  #print("End of l")

  #print("squareList[] = " + str(squareList))
  return squareList


#This function will take in the game board. It will itterate through it and any avaiable spot e.g. spot == 0 it will create a domain for. This will be stored in a dictionary with the key = coordinates of the spot (0-based). It will then use that spot to evaulate a domain and store that list as the value in the dictionary.
#ex. domainDict = {key=(0,0) value= [3,7,9]}
def createDomain(gameBoard, colList, rowList, squareList):
  domainDict = {}
  #Indexing is normal x,y cordinates. but for colList its
  #
  #ex. spot (0,3) = 4. in colList we get that by saying colList[0][2] so y is -1
  # same spot but in rowList we get by saying rowList[2][0] so reverse order and x is -1.
  # same spot but for squareList all we need to know somehow is that (0,2) - (2,2) is in square 1. if the squares are organized like this
  # 0 1 2
  # 3 4 5
  # 6 7 8

  #This will loop us through all 81 spots on the board and create a domain for each of them based on the 3 catagory lists we pass to this function. I will be row counter. J will be column counter. so I is the y coordinate and j is the x coordinate.
  for i in range(0, 9):
    for j in range(0, 9):
      domain = []
      #So first we need to check if the value of the game board is 0 because those are the only ones we need to create domains for.
      if gameBoard[(i*9) + j] == 0:

        #Now we need to create a dictionary based on the values we have.
        #k will just be a number 1-9 and we will say if k is not in all 3 of the lists then we will add k to the dicitonary

        for k in range(1, 10):

          if k not in colList[j] and k not in rowList[
              i] and k not in squareList[math.floor((i/3))*3 + math.floor((j/3))]:
            
            domain.append(k)
        if(len(domain) != 0):
         domainDict[str(i) + "," + str(j)] = domain

  # for item in domainDict:
  #   print(str(item) + " " + str(domainDict[item]) + "\n")
  return domainDict







#This function just prints a domain at a certain point.
# point is formated like ex. 0,1 or 3,3.
def getDomainAtPoint(point, domain):

  print(domain[point])
  print(len(domain[point]))
  return



def sortDomainByValueLength(domainDict):
  maxLen = 0
  domainDictKeys = []
  domainDictValues = []
  sortedDomainDict = {}

  #Iterate through the domainDict.Values and create a list we can sort of values. Also creating a max length
  for value in domainDict.values():
    domainDictValues.append(value)
    if len(value) > maxLen:
      maxLen = len(value)

  #Do the same thing for the keys. 
  for key in domainDict.keys():
    domainDictKeys.append(key)



  # Do this multiple times to find any values missed on each pass. Values that are right next to each other will be missed due to the iteration and removal of keys/value pairs. 
  while len(domainDictValues) > 0:
    # Iterate through each length of value to sort them from smallest to largest. 
    for i in range(1,maxLen+1):

      for value in domainDictValues:
        # print(value)
        if len(value) == i:
         
          # Store the location of the found key/value for access. 
          index = domainDictValues.index(value)
          
          #First lets add the found value and key at the same index into the new sorted dictionary. 
          sortedDomainDict[domainDictKeys[domainDictValues.index(value)]] = value

          #Now we need to remove both that key and value from their respective lists so we dont find them again thought iteration.
          domainDictValues.remove(value)
          domainDictKeys.remove(domainDictKeys[index])

  
  return sortedDomainDict


#This function gets us the first key value pair in the sorted domain dictionary and reformats the key to a list of ints for further use. key_value = ([x,y],[value]) where key_value[0] = [x,y] where x is what row we are in and y is what column. 
def getFirstKeyValue(sortedDomainDict):
  
  key_value = (list(sortedDomainDict.keys())[0].replace(","," ").split(),sortedDomainDict[list(sortedDomainDict.keys())[0]])
  
  # print(key_value)
  return key_value



#Need to now fix if there are 0 values in the domain we need to not include that value in the domain creation. This will make the if condition in test move work properly.



def testMove(gameBoard,move,rowList,colList,squareList,domain):
  start_domain = list(domain)

  # print(start_domain)
  # print(len(start_domain))

  temp_rowList = list(rowList)
  temp_colList = list(colList)
  temp_squareList = list(squareList)
  temp_gameBoard = list(gameBoard)

  row = int(move[0][0])
  column = int(move[0][1])
  move_val = int(move[1][0])

  # print("Before - \n")
  # print(temp_rowList[row])
  # print(temp_colList[column])
  # print(temp_squareList[math.floor((row/3))*3 + math.floor((column/3))])


  temp_rowList[row][column] = move_val
  temp_colList[column][row] = move_val
     
  temp_squareList[math.floor((row/3))*3 + math.floor((column/3))][(row % 3)*3 + (column % 3)] = move_val
  temp_gameBoard[(row*9)+column] = move_val
  new_domain = createDomain(temp_gameBoard,temp_colList,temp_rowList,temp_squareList)
  
  # print(len(list(new_domain)))
  if (len(list(new_domain)) < len(start_domain)-1):

    return False


  # print("After - \n")
  # print(temp_rowList[row])
  # print(temp_colList[column])
  # print(temp_squareList[math.floor((row/3))*3 + math.floor((column/3))])




  return True

def updateDomain(gameboard,move,rowList,colList,squareList,domain):
  print(testMove(gameboard,move,rowList,colList,squareList,domain))
  return





# def findLostVal(originalDict, sortedDict):
#   for value in originalDict:
#     if value not in sortedDict:
#       return value



def main():

  colList = createListofColumns(gameBoard1)
  rowList = createListofRows(gameBoard1)
  squareList = createListofSquares(rowList)
  sortedDomainDict = sortDomainByValueLength(createDomain(gameBoard1, colList, rowList, squareList))
  # testMove(sortedDomainDict.values[0])
  # values = sortedDomainDict.values()
  key_value = getFirstKeyValue(sortedDomainDict)
  updateDomain(gameBoard1,key_value,rowList,colList,squareList,sortedDomainDict)

  #This gives us a the key_value pair at the beginning of the sorted dictionary. Now we need to be able to use this key, disect it, to know what column or row to update. 
  





 



main()


# What we have -
# 
# Domain creation given current board
# Sorting of this domain for MRV
# Values in the sorted domain dict are in order from left to right and then up and down so tie breaking is already in place
# 
#


#Program execution from this point:
  # First we need to pick the first point in the sorted dictionary.
  # Assign that point (key) the first value in the list (value)
  # Remove any empty key/value pairs from the domain dict and the key/value pair from the point we just added.
  #  If more than one key/value pair (the one we assigned a value) is removed, we know we overlapped another domain and failed. 


# Issues we might run into:
# 
# 
# 

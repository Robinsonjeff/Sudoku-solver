import math
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
  0, 8, 8, 0, 0, 0, 4, 9, 0, 5, 0, 1, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0,
  3, 0, 0
]


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
  # same spot but for squareList all we need to know somehow is that (0,3) is in square 1. if the squares are organized like this
  # 1 2 3
  # 4 5 6
  # 7 8 9

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
              i] and k not in squareList[math.floor((i + j) / 3)]:
            domain.append(k)
        domainDict[str(i) + "," + str(j)] = domain

  for item in domainDict:
    print(str(item) + " " + str(domainDict[item]) + "\n")
  return domainDict


#This function just prints a domain at a certain point.
# point is formated like ex. 0,1 or 3,3.
def getDomainAtPoint(point, domain):

  print(domain[point])
  print(len(domain[point]))


def main():

  colList = createListofColumns(gameBoard1)
  rowList = createListofRows(gameBoard1)
  squareList = createListofSquares(rowList)
  createDomain(gameBoard1, colList, rowList, squareList)



main()


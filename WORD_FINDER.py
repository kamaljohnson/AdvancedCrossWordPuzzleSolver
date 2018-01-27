import WordClassifier as wc
import main as m
def Find():
    mainDic = wc.takeIN()
    boardData = m.getInput()
    wordsInPuzzel = []
    for i in range(len(boardData)):
        for j in range(len(boardData)):
            R_currWord = boardData[i][j]
            D_currWord = R_currWord
            S_currWord = R_currWord
            searchWordList = mainDic[R_currWord]
            q = 0
            flagR = 0
            flagD = 0
            flagS = 0
            next = False
            while next == False:
                print(searchWordList)
                print(R_currWord)
                print(D_currWord)
                print(S_currWord)
                q+=1
                if q+i >=len(boardData[0]) and q+j >=len(boardData[0]):
                    break
                if flagR == 0 and q+j<len(boardData[0]):
                    R_currWord += boardData[i][j+q]
                if flagD == 0 and q+i<len(boardData[0]):
                    D_currWord += boardData[i+q][j]
                if flagS == 0 and q+j<len(boardData[0]) and q+i<len(boardData[0]):
                    S_currWord += boardData[i+q][j+q]
                tempList = []
                for word in searchWordList:
                    if word == R_currWord or word == D_currWord or word == S_currWord:
                        print("present")
                        wordsInPuzzel.append(word)
                        searchWordList.remove(word)
                    if word < R_currWord:
                        flagR = 1
                    if word < D_currWord:
                        flagD = 1
                    if word < S_currWord:
                        flagS = 1
                    if(flagS + flagD + flagR == 3):
                        next = True
                        break
                searchWordList = tempList
    print(wordsInPuzzel)
Find()

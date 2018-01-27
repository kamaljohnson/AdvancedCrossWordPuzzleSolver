#the code to classify different words into groups
def takeIN():
    mainDic = {}
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for l in letters:
        mainDic[l] = []
    wlist = input("Enter :").split(" ")
    for i in range(len(wlist)):
        wl = list(wlist[-1])
        mainDic[wl[0]].append(wlist[-1])
        wlist.pop()
    for l in letters:
        mainDic[l].sort()
    return mainDic








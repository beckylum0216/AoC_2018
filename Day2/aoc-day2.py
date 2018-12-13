import re
from typing import List, Any


class InventoryConundrum:
    theInput = []
    twoResult = []
    threeResult = []


    @classmethod
    def FileOpen(self, fileName):

        theFile = open(fileName, "r")
        theContent = theFile.readlines()

        for ii in theContent:
            tempArray = list(map(str, ii.strip()))
            for jj in tempArray:
                count = self.GetCountNum(ii.strip(), jj)
               # print('count: ', count)
                if count == None:
                    #print('running zero...', jj)
                    tempVar = {ii.strip(): {jj: 1}}
                    #print("tempVar: ", tempVar)
                    self.theInput.append(tempVar)
                else:
                    print('running non zero...', jj)
                    inputVar = {ii.strip(): {jj: count}}
                    #print(inputVar)
                    refVar = self.GetReferenceValue(inputVar)
                    #print(refVar)
                    count += 1
                    tempVar = {ii.strip(): {jj: count}}
                    self.theInput[refVar].update(tempVar)

        theFile.close()

    @classmethod
    def GetReferenceValue(self, inputVar):
        for ii, dictionary in enumerate(self.theInput):
            print(ii, dictionary, inputVar)
            if dictionary == inputVar:
                #print("dictionary:", ii)
                return ii


    @classmethod
    def GetDictionaryValue(self, inputVar, inputElement):
        for ii in self.theInput:
            if ii == inputVar:
                #print(self.theInput[refNnum].get(inputElement))
                return True
            else:
                return False

    @classmethod
    def GetCountNum(self, inputVar, inputNum):
        if len(self.theInput) == None:
            return None
        else:
            print("num of records", len(self.theInput))
            for ii in self.theInput:
                for aa, bb in ii.items():
                    if aa == inputVar:
                        print("found first key...", aa, inputVar )
                        for kk, jj in bb.items():
                            print(kk, jj, inputNum)
                            if  kk == inputNum:
                                print("Found",jj)
                                return jj
                            else:
                                print(False)
                    #else:
                        #print("not found...", aa, inputVar)

    @classmethod
    def PrintInput(self):
        for ii in self.theInput:
            for key, value in ii.items():
                    print("index: ", key ," Value: ", value)

    @classmethod
    def WriteFile(self):
        file = open('result.txt', 'w')
        for ii in self.theInput:
            for aa, bb in ii.items():
                for jj, kk in bb.items():
                    theString = aa + " , " + jj + " , " + str(kk) + "\n"
                    file.write(theString)

        file.close()

    @classmethod
    def GetResult(self):
        for ii in self.theInput:
            for aa, bb in ii.items():
                for jj, kk in bb.items():
                    if len(self.twoResult) == 0:
                        twoTemp = {aa.strip(): {kk: 1}}
                        self.twoResult.append(twoTemp)
                        print("ran adding two...")
                    else:
                        for zz in self.twoResult:
                            for xx, yy in zz.items():
                                    #print(aa, xx)
                                    if aa == xx:
                                        continue
                                    else:
                                        if kk == 2:
                                            twoTemp = {aa.strip():{kk:1}}
                                            self.twoResult.append(twoTemp)
                                            print("ran twoResult...")

                    if len(self.threeResult) == 0:
                        threeTemp = {aa.strip(): {kk: 1}}
                        self.threeResult.append(threeTemp)
                        print("ran adding three...")
                    else:
                        for ff in self.threeResult:
                            for gg, hh in ff.items():

                                    #print(aa, gg)
                                    if aa == gg:
                                        continue
                                    else:
                                        if kk == 3:
                                            threeTemp = {aa.strip():{kk:1}}
                                            self.threeResult.append(threeTemp)
                                            print("ran threeResult...")
    @classmethod
    def PrintResult(self):
        for ii in self.twoResult:
            print(ii)

        for jj in self.threeResult:
            print(jj)

if __name__ == '__main__':
    fileNamu = 'aoc-day2-input.txt'
    theInventory = InventoryConundrum()
    theInventory.FileOpen(fileNamu)
    theInventory.WriteFile()
    theInventory.GetResult()
    theInventory.PrintResult()


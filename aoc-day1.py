
class ChronalCalibration:
    theInput = []
    theResult = 0
    theDouble = {'blah' : 1}
    partTwo = 0


    @classmethod
    def FileOpen(self, fileName):
        theFile = open(fileName, "r")
        theContent = theFile.readlines()
        for ii in theContent:
            self.theInput.append(int(ii))

    @classmethod
    def ChronosFrequency(self):
        for ii in self.theInput:
            self.theResult += ii

            if str(self.theResult) in self.theDouble:
                return self.theResult
            else:
                self.theDouble.update({str(self.theResult): 1})


if __name__ == '__main__':
    #fileNamu = 'aoc-day1-input.txt'
    fileNamu = 'testCase.txt'
    theChronos = ChronalCalibration()
    theChronos.FileOpen(fileNamu)
    print(theChronos.ChronosFrequency())



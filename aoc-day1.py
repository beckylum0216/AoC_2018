
class ChronalCalibration:
    theInput = []
    theResult = 0

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
        return self.theResult

if __name__ == '__main__':
    fileNamu = 'aoc-day1-input.txt'
    theChronos = ChronalCalibration()
    theChronos.FileOpen(fileNamu)
    theChronos.ChronosFrequency()
    print(theChronos.theResult)



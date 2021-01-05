import numpy as np
import sys
N, M = map(int, input().split())
if M == 0:
    print(1)
    sys.exit(0)
blueIndex = list(map(int, input().split()))
blueIndex.sort()

blueIndex.insert(0, 0)
blueIndex.append(N + 1)

blueIndexDiff = np.diff(blueIndex)
whiteLenListWithZero = list(map(lambda x: x-1, blueIndexDiff))
whiteLenList = [i for i in whiteLenListWithZero if i != 0]
if len(whiteLenList) == 0:
    print(0)
    sys.exit(0)
min = np.amin(whiteLenList)

result = 0
for whiteLen in whiteLenList:
    surplus = whiteLen % min
    if surplus == 0:
        result += whiteLen // min
    else:
        result = result + whiteLen // min + 1
print(result)

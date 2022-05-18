# https://softeer.ai/practice/result.do?eventIdx=1&submissionSn=SW_PRBL_SBMS_57198&psProblemId=408#hold

speed = list(map(int, input().split()))

asc = False
desc = False

for i in range(len(speed)-1):
    if speed[i] < speed[i+1]:
        asc = True
    if speed[i] > speed[i+1]:
        desc = True

if asc == True and desc == True:
    print("mixed")
else:
    if asc == True and desc == False:
        print("ascending")
    elif asc == False and desc == True:
        print("descending")
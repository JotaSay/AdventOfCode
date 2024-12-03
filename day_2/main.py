#we need to take in the file line by line and split the reports by levels. then we will comparee the first report with the second one until the second one hits null
# if ther are deviations <1 or > 3 then the report is unsafe and dont count


#update: with the problem dampener we are basically allowed to remove one of the levels, so why not try removing one of the lines and re running the test
def main():
    print(countSafeReports("levels.txt"))

def countSafeReports(filename):
    count = 0
    with open(filename,"r") as f:
        for line in f:
            levels = line.split()
            if determineSafety(levels,True):
                count+=1
    return count

def determineSafety(levels,damp):
    positive = None
    for i in range(1,len(levels)):
        diff = int(levels[i])-int(levels[i-1])
        if i ==1:
            positive = True if diff >0 else False
        if positive is None or (positive and diff<0) or (not positive and diff>0) or diff==0 or abs(diff)>3:
            #here we look to see whether or not removing a number from the report will generate a better result
            if damp:
                for i in range(len(levels)):
                    if determineSafety(levels[0:i]+levels[i+1::],False):
                        return True
            return False

    return True

if __name__ == "__main__":
    main()
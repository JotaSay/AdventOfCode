import heapq
def main():
    #need to iterate over the lines line by line and create a ds. Maybe a minheap and we keep popping into the minheap, same thing for the other side
    #go thru all of the numbers
    # while the minheaps are still full get the abs value between them and add em to the end result, return end result
    file_name = "/testdox.txt"
    arr_1,arr_2,arr_2_occurences = gatherNums(file_name)
    print(calcDifference(arr_1,arr_2,arr_2_occurences))

def gatherNums(file:str)-> list[list]:
    #take in the file and gather the nums in sorted order
    #task two, take into account similarity score
    arr_1 = []
    arr_2 = []
    arr_2_occurences = {}
    with open(file,"r") as f:
        for line in f:
            num1,num2 = line.split()
            if num1 is not None and num2 is not None:
                heapq.heappush(arr_1,int(num1))
                heapq.heappush(arr_2,int(num2))
                arr_2_occurences[int(num2)] = arr_2_occurences.get(int(num2),0) + 1
    return arr_1,arr_2, arr_2_occurences


def calcDifference(arr_1:list,arr_2:list,arr_2_occurences):
    #loop thru both arrays and get the abs value in order to add to difference
    #add in task two and also for everynumber calc the score
    difference = 0
    sim_score = 0
    while arr_1 and arr_2:
        val_1,val_2 = heapq.heappop(arr_1),heapq.heappop(arr_2)
        difference += abs(val_1-val_2)
        sim_score += val_1 * arr_2_occurences.get(val_1,0)
    return difference, sim_score


if __name__ == "__main__":
    main()
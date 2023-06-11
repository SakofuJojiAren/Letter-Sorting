"""
Lab 01
@Author Allen Saakov 
@Date 06/06/23
"""
import os 

inputlist = ["in1.txt", "in2.txt", 
             "in3.txt", "in4.txt", "in5.txt"]

# Define a mergesort function (O(nlogn) time complexity in worst, best, and average case) 
def mergesort(list):

    if len(list) <= 1:
        return list
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    mergesort(left)
    mergesort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j] 
            j += 1
        k += 1

    while i < len(left):
        list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        list[k] = right[j]
        j += 1
        k += 1

    return list

for x in range(len(inputlist)): 

    filename = "in{}.txt".format(x + 1)

    # check to make sure all files provided are not empty
    if os.path.getsize(filename) == 0:
            print("File " + filename + " is empty, please populate file in the appropriate order")
            break
    
    # read in the input files 
    with open(filename, "r") as f:
        line = f.readlines()
        target = int(line[1])
        numbers_list = [int(num) for num in line[2].split()]
        added_items = []
        solution_found = False 
        sorted_list = mergesort(numbers_list)

        # Calculation algorthm with O(N) time complexity 
        i = 0
        j = len(sorted_list) - 1
        while j >= 0:
            if sorted_list[i] + sorted_list[j] > target:
                j -= 1 
            elif sorted_list[i] + sorted_list[j] < target:
                i += 1
            else: 
                added_items = [sorted_list[i], sorted_list[j]]
                solution_found = True 
                break

        # write out the output files
        output_file = "out{}.txt".format(x+1)
        with open(output_file, "w") as w:
            content = (str(target) + "\n" +
                "Before sorting\n" + 
                line[0] +
                line[2] + 
                "After sorting\n" + 
                line[0] + 
                ' '.join(map(str, sorted_list)) + "\n" +
                "Calculation O(N) in Lab1 after sorting\n" +
                ("Yes\n" if solution_found else "No\n") +
                ("" if not solution_found else str(added_items[0]) + "+" + str(added_items[1]) + "=" + str(target)))
            w.write(content)
        f.close()




def bin_search(lst, low, high, target):
    # get average of low and high
    mid = (low + high) // 2
    # Print mid, lst[mid], and target 
    print(f"mid: {mid}, lst[mid]: {lst[mid]}, target: {target}")
    
    if high < low:
        return -1
    elif target == lst[mid]:
        return mid
    elif target < lst[mid]:
        return bin_search(lst, low, mid - 1, target)
    else:
        return bin_search(lst, mid + 1, high, target)

if __name__ == "__main__":
    names = ['AKM','Amy','Anany','Angelina','Anna','Calvin','Daphne','Zeeshan']
    print('Searching for Alvin:', bin_search(names,0, len(names)-1,'Alvin'))
    print(f"\n")
    names = ['AKM','Amy','Anany','Angelina','Anna','Calvin','Daphne','Zeeshan']
    print('Searching for Zeeshan:', bin_search(names,0, len(names)-1,'Zeeshan'))
    print(f"\n")
    scores = [0,0,23,26,35,44,49,58,60,60,65,70,72,78,79,80,89,90,90,91,92,92,93,94,97,98,99,99,100]
    print('Searching for 94:', bin_search(scores,0, len(scores)-1,94))
def ProductSum(arr):
    
    n = len(arr)
    count = 0
    for i in range(n):
        
        if isinstance(arr[i],list):
            if i %2 == 0:
                count = count + 2 * (ProductSum(arr[i]))
            elif i%2 == 1:
                count = count + 3 * (ProductSum(arr[i]))
            continue
        count = count + arr[i]
        
    
    return count
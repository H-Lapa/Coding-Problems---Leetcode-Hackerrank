def icecreamParlor(m, arr):
    prices = dict()

    for idx in range(len(arr)):
        price = arr[idx]
        remaining = m - price
        
        if remaining in prices:
            # Return the indices (as per the problem's requirement, 1-based index)
            return [prices[remaining] + 1, idx + 1]

        prices[price] = idx
    
    return [] 
            
def find_missing_number(arr: list) -> int:
    n = len(arr)
    sum1 = n * (n + 1) // 2
    sum2 = sum(arr)
    return sum1 - sum2
arr = [4,0,2,3]
print(find_missing_number(arr)) 

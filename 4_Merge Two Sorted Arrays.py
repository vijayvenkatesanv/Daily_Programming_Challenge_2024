def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)  

def merge(arr1, arr2, m, n):
    gap = m + n
    gap = next_gap(gap)
    
    while gap > 0:
        # Comparing elements in arr1
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        
        # Comparing elements in arr1 and arr2
        j = max(0, gap - m)
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        # Comparing elements in arr2
        if j < n:
            j = 0
            while j + gap < n:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        
        gap = next_gap(gap)

m = int(input("Enter the size of the first array (m): "))
arr1 = list(map(int, input(f"Enter {m} elements for the first array: ").split()))

n = int(input("Enter the size of the second array (n): "))
arr2 = list(map(int, input(f"Enter {n} elements for the second array: ").split()))

merge(arr1, arr2, m, n)

print("Merged first array:", arr1)
print("Merged second array:", arr2)

# 재귀로 구현
def quick_sort(li, start, end):
    # nlog(n)나오게 조정
    
    # 기저 조건
    if start >= end:
        return
    
    left = start
    right = end
    pivot = li[(start + end) // 2]

    while left <= right:
        # left
        while li[left] < pivot:
            left += 1

        # right
        while li[right] > pivot:
            right -= 1
            
        
        if left <= right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1

    quick_sort(li, start, right)
    quick_sort(li, left, end)

if __name__ == "__main__":
    li = [5, 1, 7, 4, 2, 3, 10, 8]
    quick_sort(li, 0, len(li) - 1)
    print(li)
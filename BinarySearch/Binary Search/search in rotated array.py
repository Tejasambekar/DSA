def search(arr,k):
        # if target in nums:
        #     return nums.index(target)
        # return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # if mid points the target
        if arr[mid] == k:
            return mid
        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1

        
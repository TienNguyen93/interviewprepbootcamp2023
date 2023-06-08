def countTarget (nums, target):
  def search(t):
    left, right = 0, len(nums) - 1         
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < t:
            left = mid + 1
        else:
            right = mid - 1                   
    return left

    first = search(target)
    last = search(target + 1) - 1

    if first <= last:
      return last - first + 1

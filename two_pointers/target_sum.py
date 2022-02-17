def pair_with_targetsum(arr, target_sum):
  l = 0
  r = len(arr) - 1
  cur_sum = arr[l] + arr[r]
  while l != r and target_sum != cur_sum:
    cur_sum = arr[l] + arr[r]
    if cur_sum < target_sum:
      l += 1
    elif cur_sum > target_sum:
      r -= 1

  if target_sum == cur_sum:
    return [l, r]
  else:
    return [-1, -1]

print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
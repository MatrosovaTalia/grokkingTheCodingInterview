def containsDuplicate(nums) -> bool:
        appeared = set()
        for n in nums:
            if n in appeared:
                return True
            else:
                appeared.add(n)
        return False

print(containsDuplicate([1, 2, 4, 4, 1]))
print(containsDuplicate([1, 2, 4, 3, 1]))
print(containsDuplicate([1]))
print(containsDuplicate([1, 2, 4, 4]))
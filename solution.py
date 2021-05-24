# (C) Copyright 2021 Ryan Martin <?>

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        _nums = []
        for _index in range(len(nums)):
            # TODO best idea
            #if (not (nums[_index] in _nums)):
            #   _nums.append(nums[_index])
            if (self.isame(nums[_index], _nums, \
                    len(_nums)) == len(_nums)):
                _nums.append(nums[_index])
        return len(_nums)

    def isame(self, num: int, _nums: list, \
            _len=None) -> int:
        # TODO nice syntax
        #_index = (_len != None) and _len or len(_nums)
        _index = len(_nums)
        for index in range(_index):
            if (num == _nums[index]):   return index
        return _index

# TODO del
import random

if __name__ == "__main__":
    for few in range(5):
        #_list = [random.randrange(10) for val in \
        #        range(random.randrange(10))]
        _list = [random.randrange(10) for val in range(10)]
        # TODO del
        print(_list)
        solution = Solution().removeDuplicates(_list)
        print("> %s\t" %solution)

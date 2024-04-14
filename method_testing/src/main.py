class Testing: 
    def give_first(self, nums: list[int]) -> int: 
        return nums[0]
    
    def give_first_alt(self, nums: list[int]) -> int: 
        return nums[:-1][0]
    
    def give_last(self, nums: list[int], num: int) -> int: 
        return nums[-1]
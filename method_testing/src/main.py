class Testing: 
    def give_first(self, nums): 
        return nums[0]
    
    def give_first_alt(self, nums): 
        return nums[:-1][0]
    
print(Testing().give_first([1, 2, 3]))
print(Testing().give_first_alt([1, 2, 3]))
The implementation handles the case when all numbers in array are negative.

def maxSubArraySum(a,size): 
      
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size):
        # if a[i] is negative and making curr_max + a[i] negative that, then that would be the curr_sum
        # once a positive a[i] comes, after negative curr_sum, automatically curr_sum would be a[i], which means 
        # leaving all old numbers behind.
        curr_max = max(a[i], curr_max + a[i]) 
      
        ## Notes for thinking on line:12
        ## if a[i] is bigger than curr_max + a[i], that means: my curr_max was less than or equal to zero, so adding this curr_max will not give 
        ## any benifit.... 
        ## And if curr_max + a[i] is bigger than a[i], that means adding a[i] to curr_max may leads to max array in future...
        ## ****** if curr_max + a[i] is less than curr_max, still we will update curr_max because it may leads to max_sub_array, if not max_so_far 
        ## is anyway storing max_so_far... so no issues. 
        
        # negative curr_sum would not get picked below
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 
  

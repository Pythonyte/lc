The implementation handles the case when all numbers in array are negative.

def maxSubArraySum(a,size): 
      
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size):
        # if a[i] is negative and making curr_max + a[i] negative that, then that would be the curr_sum
        # once a positive a[i] comes, after negative curr_sum, automatically curr_sum would be a[i], which means 
        # leaving all old numbers behind.
        curr_max = max(a[i], curr_max + a[i]) 
        
        # negative curr_sum would not get picked below
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 
  

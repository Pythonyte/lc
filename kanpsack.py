def calculate_max_profit(weights, profits, capacity):
    max_profit = 0
    def helper(weights, profits, capacity, profit_till_now):
        if not weights and capacity > 0:
            return
        if capacity == 0:
            nonlocal max_profit
            max_profit = max(max_profit, profit_till_now)
        if capacity > 0 and weights and profits:
            helper(weights[1:], profits[1:], capacity - weights[0], profit_till_now+profits[0])
            helper(weights[1:], profits[1:], capacity, profit_till_now)

    helper(weights, profits, capacity, 0)
    return max_profit

def calculate_max_profit_space_optimal(weights, profits, capacity):
    max_profit = 0
    def helper(curr_index, capacity, profit_till_now):
        if curr_index >= len(weights) and capacity > 0:
            return
        if capacity == 0:
            nonlocal max_profit
            max_profit = max(max_profit, profit_till_now)
        elif capacity > 0 and curr_index < len(weights):
            helper(curr_index+1, capacity - weights[curr_index], profit_till_now+profits[curr_index])
            helper(curr_index+1, capacity, profit_till_now)

    helper(0, capacity, 0)
    return max_profit

################################################################################################################################

def knapsack_recursive(profits, weights, capacity, cur_index):
    # Base Conditions
    if cur_index >= len(weights) or capacity < 0:
        return 0

    # Idea: Either include curr_index weight in your solution or exclude it
    profit_when_include = 0
    if weights[cur_index] <= capacity:
        profit_when_include = profits[cur_index] + knapsack_recursive(profits, weights, capacity-weights[cur_index], cur_index+1)

    profit_when_exclude = knapsack_recursive(profits, weights, capacity, cur_index+1)

    return max(profit_when_exclude, profit_when_include)


def knapsack_recursive_memoized(dp, profits, weights, capacity, cur_index):
    # Base Conditions
    if cur_index >= len(weights) or capacity < 0:
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[cur_index][capacity] != -1:
        return dp[cur_index][capacity]

    # Idea: Either include curr_index weight in your solution or exclude it
    profit_when_include = 0
    if weights[cur_index] <= capacity:
        profit_when_include = profits[cur_index] + knapsack_recursive(profits, weights, capacity-weights[cur_index], cur_index+1)

    profit_when_exclude = knapsack_recursive(profits, weights, capacity, cur_index+1)

    dp[cur_index][capacity] = max(profit_when_exclude, profit_when_include)
    return dp[cur_index][capacity]

################################################################################################################################

 """
 Let’s try to populate our dp[][] array from the above solution by working in a bottom-up fashion. 
 Essentially, we want to find the maximum profit for every sub-array and every possible capacity. 
 This means that dp[i][c] will represent the maximum knapsack profit for capacity ‘c’ calculated from the first ‘i’ items.

So, for each item at index ‘i’ (0 <= i < items.length) and capacity ‘c’ (0 <= c <= capacity), we have two options:

Exclude the item at index ‘i.’ In this case, we will take whatever profit we get from the sub-array excluding this item => dp[i-1][c]
Include the item at index ‘i’ if its weight is not more than the capacity. In this case, we include its profit plus whatever profit we 
get from the remaining capacity and from remaining items => profit[i] + dp[i-1][c-weight[i]]

Finally, our optimal solution will be maximum of the above two values: 
 """
  

# Space O(N*C) Time O(N*C)
def knapsack_bottomup(profits, weights, capacity):
    if capacity == 0 or not profits or not weights:
        return 0
    n = len(profits)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for row in range(n):
        dp[row][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for cap in range(capacity+1):
        if weights[0] <= cap:
            dp[0][cap] = profits[0]

    for r in range(1,n):
        for c in range(1, capacity+1):
            profit_when_include, profit_when_exclude = 0,0
            if weights[r] <= c:
                # include the item, if it is not more than the capacity
                profit_when_include = profits[r] + dp[r-1][c-weights[r]]
            
            # exclude the item
            profit_when_exclude = dp[r-1][c]
            
            # take maximum
            dp[r][c] = max(profit_when_include, profit_when_exclude)

    return dp[n-1][capacity]

def solve_knapsack(profits, weights, capacity):

    # Since we have two changing values (capacity and currentIndex) in our recursive function
    # knapsackRecursive(), we can use a two-dimensional array to store the results of all the solved
    # sub-problems.
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return knapsack_recursive_memoized(dp, profits, weights, capacity, 0)



if __name__ == '__main__':
    data = [
        ([2, 3, 1, 4], [4, 5, 3, 7], 5),
        ([2, 3, 1, 4], [4, 5, 3, 7], 10),
        ([2, 3, 1, 4], [4, 5, 3, 7], 8),
        ([2, 3, 1, 4, 2], [4, 5, 3, 7, 8], 8),
        ([2, 3, 1, 4, 2], [4, 5, 3, 7, 8], 4)
    ]

    for weights, profits, capacity in data:
        print(calculate_max_profit_space_optimal(weights, profits, capacity),
              "<>", calculate_max_profit_space_optimal(weights, profits, capacity),
              "<>", solve_knapsack(profits, weights, capacity),
              '<>', knapsack_bottomup(profits, weights, capacity)
              )







### OUTPUT
10 <> 10 <> 10 <> 10
19 <> 19 <> 19 <> 19
15 <> 15 <> 15 <> 15
20 <> 20 <> 20 <> 20
12 <> 12 <> 12 <> 12













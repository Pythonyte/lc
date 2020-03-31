class Solution:
    def leastIntervalSOL1(self, tasks: List[str], n: int) -> int:
        def get_extremes(tasks):
            from collections import defaultdict
            extreme, extreme_tasks = 0, 0
            freqs = defaultdict(int)
            for task in tasks:
                freqs[task] += 1
                extreme = max(extreme, freqs[task])
            for task, freq in freqs.items():
                if freq == extreme:
                    extreme_tasks += 1
            return extreme, extreme_tasks
            
        extreme, spill_over = get_extremes(tasks)
        total_windows = extreme - 1
        window_length = n + 1
        ans = total_windows * window_length + spill_over
        return ans if ans > len(tasks) else len(tasks)
    
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def get_extremes(tasks):
            from collections import defaultdict
            extreme, extreme_tasks = 0, 0
            freqs = defaultdict(int)
            for task in tasks:
                freqs[task] += 1
                extreme = max(extreme, freqs[task])
            for task, freq in freqs.items():
                if freq == extreme:
                    extreme_tasks += 1
            return extreme, extreme_tasks
            
        extreme, extreme_tasks = get_extremes(tasks)
        total_windows = extreme - 1
        window_length = n - (extreme_tasks - 1)
        avialable_places = total_windows * window_length
        
        total_fillers = len(tasks) - extreme_tasks*extreme 
        idle_places_after_filling = max(0, avialable_places - total_fillers)

        return idle_places_after_filling + len(tasks) 
    

        # Attention on the above, if the filler tasks are more than the noOfPlaces avail, we dont need to extra idle
        # places, thus we take the max against 0.
        # Because idlePlaces are only required to be filled in the windows, not at the end.
        #e: 4, g : 4, z : 1 & gap = 3
        # 1st step => e, _, _, _, e, _, _, _, e, _, _, _, e, --end--
        # observe the # of windows with _'s are maxFreq - 1, i.e : 4 - 1 = 3

        # 2nd step => e, g, _, _, e, g, _, _, e, g, _, _, e, g
        # observe that the len of each window is gap - (maxFreqtask - 1), i.e : 3 - 1 = 2
        # which makes the #ofavailPlaces = 3 * 2 = 6.

        # 3rd step => e, g, z, _, e, g, _, _, e, g, _, _, e, g # only one filler task
        # 4th step => e, g, z, _, e, g, _, _, e, g, _, _, e, g #
        # observe #of idle places left after using filler tasks are max (0, 6 - 1) = 5.

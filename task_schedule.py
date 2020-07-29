class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = list(collections.Counter(tasks).values())
        max_num = max(count)
        max_num_count = count.count(max_num)
        return max(len(tasks), (n+1)*(max_num-1)+ max_num_count)
# https://leetcode.com/problems/number-of-recent-calls/description/

class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        results = []

        for i in reversed(self.counter):  # Cek dari yg paling besar (belakang)
            if (i <= t) and (i >= t-3000):
                results.append(i)
            else:
                break
            
            return len(results)
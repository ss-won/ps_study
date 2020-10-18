class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = '1'
        for i in range(n-1):
            prev = 0
            count = 0
            next_sequence = ''
            for i, v in enumerate(sequence):
                if i == 0:
                    prev = v
                    count = 1
                    continue
                if prev == v:
                    count += 1
                else:
                    next_sequence += str(count) + str(prev)
                    prev = v
                    count = 1
            next_sequence += str(count) + str(prev)
            sequence = next_sequence
        return sequence
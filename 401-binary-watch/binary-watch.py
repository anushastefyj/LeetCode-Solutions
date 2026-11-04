class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if turnedOn > 8:
            return []
        res = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
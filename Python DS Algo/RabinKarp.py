"""
Rabin-Karp string search using rolling hash.
"""
class RabinKarp:
    @staticmethod
    def search(text, pattern):
        d, q = 256, 101  # d: alphabet size, q: prime
        n, m = len(text), len(pattern)
        h, p, t = 1, 0, 0
        for i in range(m-1):
            h = (h*d) % q
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q
        for i in range(n-m+1):
            if p == t:
                if text[i:i+m] == pattern:
                    return i
            if i < n-m:
                t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
                if t < 0:
                    t += q
        return -1
# Example usage:
# print(RabinKarp.search("abcdef", "cde")) 
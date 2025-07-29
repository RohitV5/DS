"""
Common bit manipulation tricks.
Includes: is_power_of_two, count_set_bits.
"""
class BitManipulation:
    @staticmethod
    def is_power_of_two(n):
        return n > 0 and (n & (n-1)) == 0
    @staticmethod
    def count_set_bits(n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
# Example usage:
# print(BitManipulation.is_power_of_two(8))
# print(BitManipulation.count_set_bits(7)) 
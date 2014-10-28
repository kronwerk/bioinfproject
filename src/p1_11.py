from consts import P_TO_N4
from consts import N_TO_P4
from consts import BASE4


def pattern_to_number(pattern):
    if not pattern:
        return 0
    return pattern_to_number(pattern[:-1]) * BASE4 + P_TO_N4[pattern[-1]]

def number_to_pattern(number, k):
    if k < 1:
        return ''
    return "".join([number_to_pattern(number / BASE4, k-1), N_TO_P4[number % BASE4]])

def ComputingFrequencies(Text, k, N = None):
    if not N:
        N = pow(4, k)
    FrequencyArray = [0] * N
    for i in range(len(Text) - k + 1):
        Pattern = Text[i : i + k]
        j = pattern_to_number(Pattern)
        FrequencyArray[j] += 1
    return FrequencyArray

def FasterFrequentWords(Text, k, t = 0):
    FrequencyArray = ComputingFrequencies(Text, k)
    maxCount = max(FrequencyArray)

    FrequentPatterns = set()
    if maxCount >= t:
        for i in range(pow(4, k)):
            if FrequencyArray[i] == maxCount:
                FrequentPatterns.add(number_to_pattern(i, k))
    return FrequentPatterns

if __name__ == "__main__":
    print pattern_to_number("CGTAGCGACCAATCCCAG")
    print number_to_pattern(7231, 10)
    for i in ComputingFrequencies("ATACCTTGTAGCTTGGCAGAGAGGCGGCTGTGCGATTGTGGCAGTGACTCACAGGTGCGACAGCTCGGGCCAGCTCTCGGGAAATATCCCAGTATCTAATTTTATTTCAGTTGAGGAACCATAGCCTGAAGAAGAGTATCCTTCACTCGATGCCCTAAGGTGATAACGAGGTCCGACAAAGCTCTCCAAATCCCACCGCTACATAGAACGTCTTTAGTCCATTCGTCCTAGGATCAAAAAACCGCCGTCCGTGTGATTACAGAGCGGCGTATCTTGCCAATCAACAGAATGACCGGACAGGAGTAATGTAAGGTGAAGCGCCAACACACACGCGTTAGGTTCTACCACGTTGCGGTCTTCTTAAAGCCTGATTAGGTCATGGACCAGAAGGTGTAAACTAACTGAATATCACTCAATTTTAGAGACCCGAGAGATCGGACTGTCATTCCCAGAATTACGTCTATATCTTGGGGTCCACATCGAGGACGGGGGGCCATTGATTGCTAGTAAGTTCTCCTCTCAGGTTGGGACTACCTTCCCGGCCCGAACCCCCACTGCTCCGGTTGTCAGCGCGTGCGAGAAACCACATGAAAAATCAGCATTTTAAACAGATAAATTTGAGCCCGGGATTCTAGGCATCATTTTCATGTACTATCCCGCGATTACGTCACGGGTTCATGTAGGGAGGTGCATTTTGACGTTTGGG", 8):
        print i,
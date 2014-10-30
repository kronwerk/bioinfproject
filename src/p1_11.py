from util import pattern_to_number, number_to_pattern

class FasterFrequentCounter(object):
    def __init__(self):
        self.patterns_found = set()

    def ComputingFrequencies(self, Text, k, N = None):
        self.N = N and N or pow(4, k)
        FrequencyArray = [0] * self.N
        for i in range(len(Text) - k + 1):
            Pattern = Text[i : i + k]
            j = pattern_to_number(Pattern)
            self.patterns_found.add(Pattern)
            FrequencyArray[j] += 1
        return FrequencyArray

    def FasterFrequentWords(self, Text, k, t = 0):
        FrequencyArray = self.ComputingFrequencies(Text, k)
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
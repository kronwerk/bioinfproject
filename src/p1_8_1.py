from p1_11 import FasterFrequentCounter
from util import pattern_to_number
from consts import P_TO_N4

class FasterFrequentCounterMismatched(FasterFrequentCounter):
    def __init__(self, d):
        super(FasterFrequentCounterMismatched, self).__init__()
        self.d = d
        self.letters = P_TO_N4.keys()

    def get_mismatched(self, mismatched, d):
        if d == 0:
            return
        new_mismatched = set([])
        for base_pattern in mismatched:
            for i in xrange(len(base_pattern)):
                for l in [_ for _ in self.letters if _ != base_pattern[i]]:
                    mis_pattern = "".join([base_pattern[:i], l, base_pattern[i+1:]])
                    new_mismatched.add(mis_pattern)
        mismatched.update(new_mismatched)
        self.get_mismatched(mismatched, d - 1)

    def mark_mismatched(self, frequency_array):
        addons = {}
        for found_pattern in self.patterns_found:
            found_index = pattern_to_number(found_pattern)
            mismatched = set([found_pattern])
            self.get_mismatched(mismatched, self.d)
            for m in mismatched:
                if m not in self.patterns_found:
                    frequency_array[pattern_to_number(m)] += frequency_array[found_index]
                elif m in self.patterns_found and m != found_pattern:
                    if found_index not in addons:
                        addons[found_index] = 0
                    addons[found_index] += frequency_array[pattern_to_number(m)]
        for index, addon in addons.items():
            frequency_array[index] += addon

    def ComputingFrequencies(self, Text, k, N = None):
        FrequencyArray = super(FasterFrequentCounterMismatched, self).ComputingFrequencies(Text, k, N)
        self.mark_mismatched(FrequencyArray)
        return FrequencyArray


if __name__ == "__main__":
    f = open(r"D:\soft\devProjects\bioinfproject\data\dataset_9_4.txt")
    pattern = f.readline().strip()
    text = f.readline().strip()
    d = int(f.readline().strip())
    #print pattern, text, d
    f.close()
    #for p in pattern_pos(text, pattern, d):
    #    print p,
    #print len(pattern_pos("GCTGAATGCGCGAAGCGGCCATCTGCTGAGGCCGGATTGGCTGGTCTAAGTAGAGTTCCTGACCGGTTGGCTGTCGCCGTGGGTGCCTCAGATACCTTCAGGCTCAATTATGCTTTGAAGCTGCCATCGCCAGCTTCATCTTCGGTTATGTAGGCGAGCTCCATTAATCGGTAGCGCAGCGACAATCGAGTACTACACTATACATACGCAAACCGAGATACACGACGCGTAGCATACTCGCAATAACTTTTTATCCCGTTGACGTTCGGACCGTGACCTGAGGATGCAGCATAATTCTCGTGCTACTGAGTAATGGTGTCCCATCATGCCTCAAACACTAGTTATCGCCTAATCTAAGCTTCC", "AGCTC", 2))
    print FasterFrequentCounterMismatched(2).FasterFrequentWords("GCAACTAGAGGCCCGGCAAGCAAGCAACCCGGCAACCCGATCAGGGCAAAGGAGGAGGCTAGGCAACTAGCCCGAGGATCCCCGCTAGCCCGATCATCGCAACTAGATCGCAACTAGCTAGCCCGAGGAGGATCAGGATCGCAACTAGATCCCCGATCCTAGAGGCCCGATCCCCGAGGATCCCCGCCCGAGGGCAAATCAGGATCAGGCCCGCCCGATCCCCGCCCGGCAACTAGAGGCCCGATCCCCGCTAGATCAGGGCAACCCGCTAGATCCTAGCTAGCTAGCCCGGCAAGCAAGCAAATCAGGCCCGCCCGATCCTAGCTAGCCCGCTAGGCAACTAG", 8)
    #print FasterFrequentCounterMismatched(1).FasterFrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
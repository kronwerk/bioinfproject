from util import pattern_to_number, number_to_pattern
from p1_8_1 import FasterFrequentCounterMismatched
from p1_3_1 import reverse_complement

class FasterFrequentCounterMismatchedReversed(FasterFrequentCounterMismatched):
    def process_pattern(self, found_pattern, found_index, frequency_array, addons):
        mismatched = set([found_pattern])
        self.get_mismatched(mismatched, self.d)
        for m in mismatched:
            if m not in self.patterns_found:
                frequency_array[pattern_to_number(m)] += frequency_array[found_index]
            elif m in self.patterns_found and m != found_pattern:
                if found_index not in addons:
                    addons[found_index] = 0
                addons[found_index] += frequency_array[pattern_to_number(m)]

    def mark_mismatched(self, frequency_array):
        addons = {}
        ind_pairs = {}
        for found_pattern in self.patterns_found:
            found_index = pattern_to_number(found_pattern)
            rev_found = reverse_complement(found_pattern)
            rev_index = pattern_to_number(rev_found)
            self.process_pattern(found_pattern, found_index, frequency_array, addons)
            self.process_pattern(rev_found, rev_index, frequency_array, addons)
            ind_pairs[found_index] = rev_index
        for f, r in ind_pairs.items():
            if r not in ind_pairs:
                if f not in addons:
                    addons[f] = 0
                if r not in addons:
                    addons[r] = 0
                addons[f] += frequency_array[r]
                addons[r] += frequency_array[f]
        for index, addon in addons.items():
            frequency_array[index] += addon


if __name__ == "__main__":
    #print FasterFrequentCounterMismatchedReversed(1).FasterFrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    print FasterFrequentCounterMismatchedReversed(3).FasterFrequentWords("CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT", 9)
    #print FasterFrequentCounterMismatchedReversed(3).FasterFrequentWords("GCGCCGAGCCGATGCTGCCATGCGCCGCGATGCGACAGACAGCTGCCAGCGCCACATGCTGCGCTGCGCGCCGCCAGAGCCGAGCCCAGCCGACAGAGCCTGCTGCGCCGCGCCCAGCGCTGCGCCGATGCTGCGAGCTGCGATGCCAGCCGCCATGCTGCGCCAGCGAGACATGCTGCCAGCTGCGCCGCCGCGCGCCGCCATGCGCCTGCGATGCGATGCGCCATGCGAGCGCCTGC", 8)
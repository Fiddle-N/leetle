from collections import Counter

def solve(ransomNote, magazine):
  # wrong way around in Leetle
  return Counter(magazine) <= Counter(ransomNote)

# Read from the file words.txt and output the word frequency list to stdout.

# This beats 77% of solutions by CPU on leetcode
cat words.txt \
  | tr ' ' '\n' \
  | grep -E -v '^$' \
  | awk '{ seen[$0]++ }; END { for (i in seen) print i, seen[i] }' \
  | sort -k 2 -r -n

# Readme

## Instruction

### Find a number sequence inside an array of numbers

```go
Int [] main = new int[] {20, 7, 8, 10, 2, 5, 6} // non repeating numbers
Int [] seq = new int [] {1,4}
sequenceExists(main, [7,8]) ⇒ true
sequenceExists(main, [8, 7]) ⇒ false
sequenceExists(main, [7, 10]) ⇒ false
```

## Solution

There are 2 functions written in `main.go`. One function assuming that the sequences only contains 2 number, the other function assuming that the sequence can contains 2 or more numbers.

Both function has a time complexity of O(n).
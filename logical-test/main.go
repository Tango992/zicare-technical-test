package main

import (
	"fmt"
	"slices"
)

func main() {
	main := []int{20, 7, 8, 10, 2, 5, 6}
	seq := []int{7, 8, 10}

	result := sequenceExists(main, seq)
	fmt.Println(result)
}

/*
	Assuming sequence contains 2 numbers or more
*/
func sequenceExists(main, seq []int) bool {
	mainLength := len(main)
	seqLength := len(seq)

	for i := 0; i < (mainLength-seqLength); i++ {
		mainParsed := main[i:seqLength+i]
		if slices.Equal(mainParsed, seq) {
			return true
		}
	}
	return false
}

/*
	Assuming sequence only contains 2 numbers
*/
// func sequenceExists(main, seq []int) bool {
// 	lengthMinusOne := len(main)-1
	
// 	for i := range main[:lengthMinusOne] {
// 		if seq[0] == main[i] && seq[1] == main[i+1] {
// 			return true
// 		}
// 	}
// 	return false
// }

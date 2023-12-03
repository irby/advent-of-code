package main

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func Test_PartOne(t *testing.T) {
	input := readFile("sample.txt")
	result := partOne(input)
	assert.Equal(t, 8, result)
}

func Test_PartTwo(t *testing.T) {
	input := readFile("sample.txt")
	result := partTwo(input)
	assert.Equal(t, 2286, result)
}

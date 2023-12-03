package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var configuration1 = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

func getEmptyTotals() map[string]int {
	return map[string]int{"red": 0, "green": 0, "blue": 0}
}

func getColorAndQuantity(selection string) (string, int) {
	parts := strings.Fields(selection)
	quantity, _ := strconv.Atoi(parts[0])
	color := parts[1]
	return color, quantity
}

func isGameValid(game string) bool {
	maxes := configuration1
	rounds := strings.Split(game, ";")
	for _, round := range rounds {
		totals := getEmptyTotals()
		draws := strings.Split(round, ",")
		for _, selection := range draws {
			color, quantity := getColorAndQuantity(selection)
			totals[color] += quantity
			if totals[color] > maxes[color] {
				return false
			}
		}
	}
	return true
}

func getGamePower(game string) (map[string]int, int) {
	total := 1
	maxes := getEmptyTotals()
	rounds := strings.Split(game, ";")
	for _, round := range rounds {
		totals := getEmptyTotals()
		draws := strings.Split(round, ",")
		for _, selection := range draws {
			color, quantity := getColorAndQuantity(selection)
			totals[color] += quantity
			maxes[color] = max(maxes[color], totals[color])
		}
	}

	for _, value := range maxes {
		total *= value
	}
	return maxes, total
}

func getGameAndNumber(gameWithNum string) (string, int) {
	split1 := strings.Split(gameWithNum, ":")
	gameNum, _ := strconv.Atoi(strings.Fields(split1[0])[1])
	return split1[1], gameNum
}

func partOne(input []string) int {
	validGameIDs := []int{}
	for _, line := range input {
		game, num := getGameAndNumber(line)
		if isGameValid(game) {
			validGameIDs = append(validGameIDs, num)
		}
	}
	return sum(validGameIDs)
}

func partTwo(input []string) int {
	result := 0
	for _, line := range input {
		game, _ := getGameAndNumber(line)
		_, power := getGamePower(game)
		result += power
	}
	return result
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func sum(nums []int) int {
	result := 0
	for _, num := range nums {
		result += num
	}
	return result
}

func readFile(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return []string{}
	}
	defer file.Close()

	var input []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	return input
}

func main() {
	input := readFile("input.txt")

	fmt.Println("part 1:", partOne(input))
	fmt.Println("part 2:", partTwo(input))
}

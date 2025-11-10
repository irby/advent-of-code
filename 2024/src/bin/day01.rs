use std::collections::HashMap;
use advent_of_code_2024::read_from_file;

fn read_input(input: &str) -> (Vec<i32>, Vec<i32>) {
    let mut left = Vec::new();
    let mut right = Vec::new();

    for line in input.lines() {
        if line.trim().is_empty() {
            continue;
        }

        let mut nums = line.split_whitespace();
        left.push(nums.next().unwrap().parse::<i32>().unwrap());
        right.push(nums.next().unwrap().parse::<i32>().unwrap());
    }

    return (left, right);
}

fn solve_part_one(input: &str) -> i32 {
    let (mut left, mut right) = read_input(input);

    // Sort the lists before doing any operations
    left.sort();
    right.sort();

    // Get the absolute value of the difference between the left and right elements
    let mut total = 0;
    for i in 0..left.len() {
        total += (left[i] - right[i]).abs();
    }

    return total;
}

fn solve_part_two(input: &str) -> i32 {
    let (left, right) = read_input(input);

    // Build a frequency map of the right list
    let mut counts = HashMap::new();
    for &num in &right {
        *counts.entry(num).or_insert(0) += 1;
    }

    // For each number in left, get its occurrence count. Take the product of the number and its occurence and
    // add it to the total.
    let mut total = 0;
    for &num in &left {
        let count = counts.get(&num).unwrap_or(&0);
        total += num * count;
    }

    return total;
}

fn main() {
    let input = read_from_file("inputs/day01.txt");

    let result_1 = solve_part_one(&input);
    println!("Part One: {}", result_1);

    let result_2 = solve_part_two(&input);
    println!("Part Two: {}", result_2)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = read_from_file("inputs/day01_test.txt");

        assert_eq!(solve_part_one(&input), 11); // expected result from problem
    }

    #[test]
    fn test_part_two() {
        let input = read_from_file("inputs/day01_test.txt");

        assert_eq!(solve_part_two(&input), 31); // expected result from problem
    }
}

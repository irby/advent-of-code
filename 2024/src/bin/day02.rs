use advent_of_code_2024::read_from_file;

fn read_input(input: &str) -> Vec<Vec<i32>> {
    input
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            line.split_whitespace()
                .map(|n| n.parse::<i32>().unwrap())
                .collect()
        })
        .collect()
}

fn solve_part_one(input: &str) -> i32 {
    let grid = read_input(input);

    return grid.iter().filter(|row| is_safe_row(row)).count() as i32;
}

fn solve_part_two(input: &str) -> i32 {
    let grid = read_input(input);

    return grid.iter().filter(|row| is_safe_with_dampener(row)).count() as i32;
}

fn is_safe_with_dampener(row: &[i32]) -> bool {
    if is_safe_row(row) {
        return true;
    }

    // Try removing a single element from row and determine if
    // altered row is safe
    for skip_index in 0..row.len() {
        let modified: Vec<i32> = row
            .iter()
            .enumerate()
            .filter(|(i, _)| *i != skip_index)
            .map(|(_, &val)| val)
            .collect();

        if is_safe_row(&modified) {
            return true;
        }
    }

    false
}

fn is_safe_row(row: &[i32]) -> bool {
    let mut direction: Option<i32> = None;

    let lower_bound: i32 = 1;
    let upper_bound: i32 = 3;

    for j in 0..row.len() - 1 {
        let current_element = row[j];
        let next_element = row[j + 1];
        let difference = current_element - next_element;
        let abs_difference = difference.abs();

        // If the direction is not alreday determined, assign
        // 1 as the direction if increasing, -1 if decreasing
        // If no difference detected, wait until the next item
        // to determine direction.
        if direction.is_none() {
            if difference > 0 {
                direction = Some(1);
            } else if difference < 0 {
                direction = Some(-1);
            }
        } else {
            // If direction is decided, if the next item goes in the opposite direction
            // of the direction, mark it unsafe.
            match direction {
                Some(1) if difference < 0 => return false,
                Some(-1) if difference > 0 => return false,
                _ => {}
            }
        }

        // If difference is outside the bounds of safety, mark it unsafe.
        if abs_difference < lower_bound || abs_difference > upper_bound {
            return false;
        }
    }

    return true;
}

fn main() {
    let input = read_from_file("inputs/day02.txt");

    let result_1 = solve_part_one(&input);
    println!("Part One: {}", result_1);

    let result_2 = solve_part_two(&input);
    println!("Part Two: {}", result_2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = read_from_file("inputs/day02_test.txt");

        assert_eq!(solve_part_one(&input), 2); // expected result from problem
    }

    #[test]
    fn test_part_two() {
        let input = read_from_file("inputs/day02_test.txt");

        assert_eq!(solve_part_two(&input), 4); // expected result from problem
    }
}

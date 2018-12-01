use std::collections::HashSet;
use std::fs::File;
use std::io::prelude::*;

fn parse_numbers_in_file(filename: &str) -> Vec<i32> {
    let mut f = File::open(filename).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("something went wrong reading the file");

    let numbers: Vec<i32> = contents
        .trim()
        .split('\n')
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    return numbers;
}

fn run_part_one() {
    let filename = "../inputs/day1.txt";
    let numbers = parse_numbers_in_file(filename);

    println!("part 1 result: {}", numbers.iter().sum::<i32>());
}

fn run_part_two() {
    let filename = "../inputs/day1.txt";
    let numbers = &parse_numbers_in_file(filename);
    let mut seen = HashSet::new();
    let mut running_sum = 0;

    loop {
        for &number in numbers {
            seen.insert(running_sum);
            running_sum += &number;

            if seen.contains(&running_sum) {
                println!("part 2 result: {}", running_sum);
                return;
            }
        }
    }
}

pub fn run(part: i32) {
    match part {
        1 => run_part_one(),
        2 => run_part_two(),
        _ => eprintln!("error: unknown part!"),
    }
}

extern crate regex;

use std::fs::File;
use std::io::prelude::*;
use std::str;

fn parse_strings_in_file(filename: &str) -> Vec<String> {
    let mut f = File::open(filename).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("something went wrong reading the file");

    let strings: Vec<String> = contents.trim().split('\n').map(|s| s.to_string()).collect();

    return strings;
}

fn get_claimed_fabric(filename: &str) -> [[i16; 1100]; 1100] {
    let claims = parse_strings_in_file(filename);
    let re = regex::Regex::new(r"#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)").unwrap();
    let mut x = [[0; 1100]; 1100];

    for claim in claims {
        for cap in re.captures_iter(&claim) {
            let col: usize = cap[1].parse().unwrap();
            let row: usize = cap[2].parse().unwrap();
            let width: usize = cap[3].parse().unwrap();
            let height: usize = cap[4].parse().unwrap();

            for i in row..row + height {
                for j in col..col + width {
                    x[i][j] += 1i16;
                }
            }
        }
    }

    return x;
}

fn run_part_one() {
    let filename = "inputs/day3.txt";
    let x = get_claimed_fabric(filename);

    let mut counter = 0;

    for i in 0..x.len() {
        for j in 0..x.len() {
            if x[i][j] >= 2 {
                counter += 1;
            }
        }
    }

    println!("part 1 answer: {}", counter);
}

fn run_part_two() {
    let filename = "inputs/day3.txt";
    let claims = parse_strings_in_file(filename);
    let re = regex::Regex::new(r"(#\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)").unwrap();
    let x = get_claimed_fabric(filename);

    for claim in claims {
        for cap in re.captures_iter(&claim) {
            let id: String = cap[1].to_string();
            let col: usize = cap[2].parse().unwrap();
            let row: usize = cap[3].parse().unwrap();
            let width: usize = cap[4].parse().unwrap();
            let height: usize = cap[5].parse().unwrap();
            let mut found = true;

            for i in row..row + height {
                for j in col..col + width {
                    if x[i][j] != 1 {
                        found = false;
                        break;
                    }
                }
            }

            if found {
                println!("part 2 answer: {}", id);
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

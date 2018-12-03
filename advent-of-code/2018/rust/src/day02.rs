extern crate counter;

use std::fs::File;
use std::io::prelude::*;

fn parse_strings_in_file(filename: &str) -> Vec<String> {
    let mut f = File::open(filename).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("something went wrong reading the file");

    let strings: Vec<String> = contents.trim().split('\n').map(|s| s.to_string()).collect();

    return strings;
}

fn run_part_one() {
    let filename = "inputs/day2.txt";
    let strings = parse_strings_in_file(filename);
    let mut a = 0;
    let mut b = 0;

    for box_id in strings {
        let mut seena = false;
        let mut seenb = false;

        let ch_counter = box_id
            .chars()
            .collect::<counter::Counter<_>>()
            .most_common_ordered();

        for &(_, counter) in ch_counter.iter() {
            if counter == 3 && !seena {
                a += 1;
                seena = true;
            } else if counter == 2 && !seenb {
                b += 1;
                seenb = true;
            }

            if seena && seenb {
                break;
            }
        }
    }

    println!("part 1 answer: {:?}", a * b);
}

fn run_part_two() {
    let filename = "inputs/day2.txt";
    let strings = parse_strings_in_file(filename);

    for i in 0..strings.len() {
        for j in i..strings.len() {
            let mut diffs = 0;
            let mut indx = 0;
            let sa = strings[i].as_bytes();
            let sb = strings[j].as_bytes();

            for k in 0..strings[i].len() {
                if sa[k] != sb[k] {
                    diffs += 1;
                    indx = k;

                    if diffs > 1 {
                        break;
                    }
                }
            }

            if diffs == 1 {
                let mut s = strings[i].to_string();
                s.remove(indx);
                println!("part 2 answer: {}", s);
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

use std::env;

mod day01;

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        1 => {
            println!("need part of problem as command line arg!")
        },
        _ => {
            let part: i32 = match args[1].parse::<i32>() {
                Ok(n) => {n},
                Err(_) => {
                    eprintln!("error: part arg is not an integer");
                    return;
                }
            };
            day01::run(part);
        }
    }
}

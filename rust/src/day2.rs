use std::fs::read_to_string;

/*
 * This is actually really ugly in rust despite
 * being the same code as used in 02.py
 */

fn valid_passwords_one(values: &Vec<(i32, i32, char, &str)>) -> i32 {
    let mut count = 0;
    for i in 0..values.len() {
        let x: i32 = values[i].0;
        let y: i32 = values[i].1;
        let c: char = values[i].2;
        let string: &str = values[i].3;
        let z: Vec<_> = string.chars().filter(|x| *x == c).collect();
        let l = z.len();
        if (l as i32) >= x && (l as i32) <= y {
            count += 1;
        }
    }
    count
}

fn valid_passwords_two(values: &Vec<(i32, i32, char, &str)>) -> i32 {
    let mut count = 0;
    for i in 0..values.len() {
        let x: i32 = values[i].0;
        let y: i32 = values[i].1;
        let c: char = values[i].2;
        let string: &str = values[i].3;

        let first = string.chars().nth(x as usize).unwrap() == c;
        let second = string.chars().nth(y as usize).unwrap() == c;
        if first^second {
            count += 1;
        }
    }
    count
}


pub fn main() {
    let input = read_to_string("./src/day2_input.txt").unwrap();
    let mut values: Vec<(i32, i32, char, &str)> = Vec::new();
    for line in input.split('\n') {
        let fs: Vec<&str> = line.split(':').collect();
        let limits: Vec<&str> = fs[0].split(' ').collect();
        let vals: Vec<&str> = limits[0].split('-').collect();
        let tpl = (vals[0].parse::<i32>().unwrap(),
                    vals[1].parse::<i32>().unwrap(),
                    limits[1].parse::<char>().unwrap(),
                    fs[1]);
        values.push(tpl); 
    }
    println!("Day 2, part 1 answer: {}", valid_passwords_one(&values));
    println!("Day 2, part 2 answer: {}", valid_passwords_two(&values));
}
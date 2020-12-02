use std::fs::read_to_string;


fn two_sum(values: &Vec<i32>) -> i32 {
    for i in 0..values.len() { 
        for j in i+1..values.len() {
            if values[i] + values[j] == 2020 {
                return values[i] * values[j];
            }
        }
    }
    0
}


fn three_sum(values: &Vec<i32>) -> i32 {
    for i in 0..values.len() {
        for j in i+1..values.len() {
            for k in j+1..values.len() {
                if values[i] + values[j] + values[k] == 2020 {
                    return values[i] * values[j] * values[k];
                }
            }
        }
    }
    0
}


pub fn main() {
    let filename = "./src/day1_input.txt";
    let input = read_to_string(filename).unwrap();
    let vals: Vec<i32> = input.split('\n').map(|x| x.trim().parse::<i32>().unwrap()).collect();
    println!("Day 1, part 1 answer: {}", two_sum(&vals));
    println!("Day 1, part 2 answer: {}", three_sum(&vals));
}
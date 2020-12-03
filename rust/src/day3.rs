use std::fs::read_to_string;


fn count_trees(right: usize, down: usize, lines: &String) -> i64 {
    let mut tree_count: i64 = 0;
    let mut current_pos = 0;
    let l: Vec<&str> = lines.lines().collect();
    let length = l[0].len();

    for i in (0..(l.len()-1)).step_by(down as usize) {
        let new_pos = (current_pos + right) % length;
        if l[i+down].chars().nth(new_pos).unwrap() == '#' {
            tree_count += 1;
        }
        current_pos = new_pos;
    }
    tree_count
}

fn count_all(lines: &String) -> i64 {
    let mut total = 1;
    let directions = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ];
    for (x, y) in &directions {
        total =  total * count_trees(*x, *y, lines);
    }
    total
}


pub fn main() {
    let lines = read_to_string("./src/day3_input.txt").unwrap();
    println!("Day 3, part 1 answer: {}", count_trees(3, 1, &lines));
    println!("Day 3, part 2 answer: {}", count_all(&lines));
}
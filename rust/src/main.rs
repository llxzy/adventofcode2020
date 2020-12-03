mod day1;
mod day2;
mod day3;

fn main() {
    let day_mains = [
        day1::main,
        day2::main,
        day3::main
    ];

    for m in &day_mains{
        m();
        println!("---")
    }
}

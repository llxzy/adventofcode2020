mod day1;
mod day2;

fn main() {
    let day_mains = [
        day1::main,
        day2::main
    ];

    for m in &day_mains{
        m();
        println!("---")
    }
}

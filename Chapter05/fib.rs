fn main() {
    let mut a: u8 = 0;
    let mut b: u8 = 1;
    println!("{}", a);
    while b <= 100 {
        println!("{}", b);
        b = a + b;
        a = b - a;
    }
}

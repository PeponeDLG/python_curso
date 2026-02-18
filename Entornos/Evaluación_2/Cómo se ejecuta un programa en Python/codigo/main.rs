use std::io;

fn main() {
    println!("Introduce tu edad: ");
    
    let mut edad = String::new();
    io::stdin().read_line(&mut edad).unwrap();
    
    if let Ok(edad) = edad.trim().parse::<u32>() {
        if edad >= 18 {
            println!("Eres mayor de edad");
        } else {
            println!("Eres menor de edad");
        }
    } else {
        println!("Por favor, introduce un número válido");
    }
}
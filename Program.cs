/*//imprimir en pantalla
Console.WriteLine("Hello, World!");

//
Console.Write("ingresa tu nombre: ");

string nombre = Console.ReadLine();

Console.WriteLine($"tu nombre es {nombre}");

*/

//Calcular promedio circuitos 1

bool x = true;
while (x)
{
    Console.Write("Ingrese la nota del primer parcial: ");
    string input1 = Console.ReadLine();
    float p1;

    while (!float.TryParse(input1, out p1))
    {
        Console.Write("Entrada inválida. Por favor, ingresa un número entero: ");
        input1 = Console.ReadLine();
    }
    ////////
    Console.Write("Ingrese la nota del primer quiz: ");
    string input2 = Console.ReadLine();
    float q1;

    while (!float.TryParse(input2, out q1))
    {
        Console.Write("Entrada inválida. Por favor, ingresa un número entero: ");
        input2 = Console.ReadLine();
    }
    /////////
    Console.Write("Ingrese la nota del segundo parcial: ");
    string input3 = Console.ReadLine();
    float p2;

    while (!float.TryParse(input3, out p2))
    {
        Console.Write("Entrada inválida. Por favor, ingresa un número entero: ");
        input3 = Console.ReadLine();
    }
    ////////
    Console.Write("Ingrese la nota del Segundo Quiz: ");
    string input4 = Console.ReadLine();
    float q2;

    while (!float.TryParse(input4, out q2))
    {
        Console.Write("Entrada inválida. Por favor, ingresa un número entero: ");
        input4 = Console.ReadLine();
    }
    /////////
    Console.Write("Ingrese la nota del tercer parcial: ");
    string input5 = Console.ReadLine();
    float p3;

    while (!float.TryParse(input5, out p3))
    {
        Console.Write("Entrada inválida. Por favor, ingresa un número entero: ");
        input5 = Console.ReadLine();
    }
    //////
    Console.Write("Ingrese la nota del cuarto parcial: ");
    string input6 = Console.ReadLine();
    float p4;

    while (!float.TryParse(input6, out p4))
    {
        Console.Write("Entrada inválida. Por favor, ingresa un número entero: ");
        input6 = Console.ReadLine();
    }

    float promedio = (p1 * 15 / 100) + (q1 * 5 / 100) + (q2 * 5 / 100) + (p2 * 25 / 100) + (p3 * 25 / 100) + (p4 * 25 / 100);
    Console.WriteLine($"promedio: {promedio}");

    Console.WriteLine();

    Console.Write("Terminar el programa? [s/n]");

    string resp = Console.ReadLine();

    if (resp == "s")
    {
        x = false;
    }
    

}
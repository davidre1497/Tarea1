using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace tarea2segundo_proyecto
{
    internal class Program
    {
        const int MaxEntradas = 4;
        static void Main(string[] args)

        {
            string numerodefabrica;
            string cedula;
            string nombre;
            string localidaddeseada = "";
            int entradasSeleccionadas = 0;
            double precioDeEntradas = 0;
            double cargosPorServicio = 1000;

            int entradasSol = 0;
            int entradasSombra = 0;
            int entradasPreferencial = 0;
            double acumuladoSol = 0;
            double acumuladoSombra = 0;
            double acumuladoPreferencial = 0;


            Console.WriteLine("Digite el numero de fabrica:");
            numerodefabrica = Console.ReadLine();
            Console.WriteLine();

            Console.WriteLine("Digite su cedula:");
            cedula = Console.ReadLine();
            Console.WriteLine();

            Console.WriteLine("Digite su nombre completo:");
            nombre = Console.ReadLine();
            Console.WriteLine();

            Console.WriteLine("Seleccione la localidad en que desea estar: 1- Sol Norte/Sur 2- Sombre Este/Oeste  3- Preferencial");
            int opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    localidaddeseada = "Sol Norte/Sur";
                    precioDeEntradas = 10500;
                    break;

                case 2:
                    localidaddeseada = "Sombre Este/Oeste";
                    precioDeEntradas = 20500;
                    break;

                case 3:
                    localidaddeseada = "Preferencial";
                    precioDeEntradas = 25500;
                    break;

                default:
                    Console.WriteLine("opcion no válida");
                    return;
            }

            while (true)
            {
                Console.WriteLine("¿Cuantas entradas desea comprar? (Maximo 4)");
                int cantidad = int.Parse(Console.ReadLine());

                if (cantidad > MaxEntradas)

                {
                    Console.WriteLine("No puede comprar más de 4 entradas. Por favor, intente de nuevo");
                }
                else
                {

                    entradasSeleccionadas = cantidad;

                    break;
                }
                }
            if (localidaddeseada != "")

            {
                double costoTotal = entradasSeleccionadas * precioDeEntradas + cargosPorServicio;
                double datosParaEstadistica = entradasSeleccionadas * precioDeEntradas;

                switch (localidaddeseada)
                {
                    case "Sol Norte/Sur":
                        entradasSol += entradasSeleccionadas;
                        acumuladoSol += datosParaEstadistica;
                        break;

                    case "Sombre Este/Oeste":
                        entradasSombra += entradasSeleccionadas;
                        acumuladoSombra += datosParaEstadistica;
                        break;

                    case "Preferencial":
                        entradasPreferencial += entradasSeleccionadas;
                        acumuladoPreferencial += datosParaEstadistica;
                        break;


                }


                Console.WriteLine("La fabrica seleccionada es: " + numerodefabrica);
                Console.WriteLine("mi cedula es: " + cedula);
                Console.WriteLine("mi nombre es: " + nombre);
                Console.WriteLine("Localidad Seleccionada: " + localidaddeseada);
                Console.WriteLine("Cantidad de entradas compradas: " + entradasSeleccionadas);
                Console.WriteLine("Costo total: " + costoTotal);
                Console.WriteLine("Cargos por Servicios:" + datosParaEstadistica);
            }
            Console.WriteLine("\nEstadísticas:");
            Console.WriteLine("Entradas Sol Norte/Sur: {entradasSol}, Acumulado: {acumuladoSol}");
            Console.WriteLine("Entradas Sombre Este/Oeste: {entradasSombra}, Acumulado: {acumuladoSombra}");
            Console.WriteLine("Entradas Preferencial: {entradasPreferencial}, Acumulado: {acumuladoPreferencial}");
            Console.ReadLine();

            }
        }
    }




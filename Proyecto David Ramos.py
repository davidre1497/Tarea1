package banco.imaginario;

import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class BancoImaginario {

    public static void main(String[] args) {
        //definicion de variables
        int op_main_menu = 0, cantidad_usuarios = 0, cedula = 0, contador = 0, op_menu_registro = 1;
        int saldo_disponible = 0;
        String nombre, apellido1, apellido2, estado_de_cuenta;
        String[][] infoPersonal = new String[0][0], infoCuenta = new String[0][0];
        Scanner scn = new Scanner(System.in);

        //menu principal
        while (op_main_menu != 5) {
            System.out.println("===== Bienvenido a Banca Imaginaria =====");
            System.out.print("1.Registrar cliente\n" + "2.Actualizar datos del cliente\n" + "3.Borrar cliente\n" + "4.Consultas\n" + "5.Definir cantidad de clientes \n" + "6.Salir\n");
            System.out.print("Ingrese a que menu quiere ingresar: ");
            op_main_menu = scn.nextInt();

            //SUBMENUS
            switch (op_main_menu) {
                case 1:
                    System.out.println("===== Registros =====");
                    System.out.print("Ingrese primero cuantos usuarios seran registrados: ");
                    cantidad_usuarios = scn.nextInt();
                    infoPersonal = new String[cantidad_usuarios][4];
                    infoCuenta = new String[cantidad_usuarios][3];
                    while (op_menu_registro == 1) {
                        if (contador <= cantidad_usuarios) {
                            System.out.print("Ingrese el numero de cedula del cliente: ");
                            cedula = scn.nextInt();
                            System.out.print("Ingrese el nombre del cliente: ");
                            nombre = scn.next();
                            System.out.print("Ingrese el primer apellido del cliente: ");
                            apellido1 = scn.next();
                            System.out.print("Ingrese el segundo apellido del cliente: ");
                            apellido2 = scn.next();
                            System.out.print("Ingrese cantidad del deposito: ");
                            saldo_disponible = scn.nextInt();
                            registroCuenta(contador, saldo_disponible, infoCuenta);
                            registroPersonal(contador, cedula, nombre, apellido1, apellido2, infoPersonal);
                            System.out.println("Registro exitoso");
                            contador += 1;
                            System.out.print("Desea hacer otro registro: 1. Si  2. No:   ");
                            op_menu_registro = scn.nextInt();
                        } else {
                            System.out.println("Numero de usuairos excedido");
                            op_menu_registro = 2;
                        }

                    }
                    break;
                case 2:
                    break;
                case 3:
                    break;
                case 4:
                    int temporal_num_cedula = 0;

                    System.out.println("===== Consultas =====");
                    System.out.print("Ingrese el numero de cedula del usuario a conusltar:  ");
                    temporal_num_cedula = scn.nextInt();
                    Consulta(temporal_num_cedula, infoPersonal, infoCuenta);
                    break;
                default:
                    op_main_menu = 5;
            }

        }
    }

    public static void registroPersonal(int numregistro, int cedula, String nombre, String apellido1, String apellido2, String[][] matriz) {
        //GUARDA LA INFORMACION PERSONAL DE LOS CLIENTES
        matriz[numregistro][0] = cedula + "";
        matriz[numregistro][1] = nombre;
        matriz[numregistro][2] = apellido1;
        matriz[numregistro][3] = apellido2;
    }

    public static void registroCuenta(int numregistro, int deposito, String[][] matriz) {
        //GUARDA LA INFORMACION DE LA CUENTA DEL CLIENTE
        Random numero_de_cuenta = new Random();
        matriz[numregistro][0] = numero_de_cuenta.nextInt(1111) + "";
        matriz[numregistro][1] = deposito + "";
        matriz[numregistro][2] = "Activa";
        System.out.println("Informacion de cuenta guardado exitosamente!");
    }

    public static void Consulta(int numerocedulatemporal, String[][] matriz, String[][] matriz2) {
        //MUESTRA EN PANTALLA LOS DATOS DEL CLIENTE CONSULATADO
        String ced = numerocedulatemporal + "";

        for (int i = 0; i < matriz.length; i++) {

            if (matriz[i][0].equals(ced)) {
                System.out.print("El usuario es: " + matriz[i][0] + " " + matriz[i][1] + " " + matriz[i][2] + " " + matriz[i][3] + " ");
                System.out.print(matriz2[i][0] + " " + matriz2[i][1] + " " + matriz2[i][2] + "\n");
            }
        }
    }

}

/**
 * 1. Registrar cliente 
 * 2. Actualizar datos del cliente 
 * 3. Borrar cliente 
 * 4. Consultas 
 * 5. Definir cantidad de clientes 
 * 6. Salir
 *
 */

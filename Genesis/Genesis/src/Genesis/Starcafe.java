package Starcafe;

import java.util.Scanner;

public class Starcafe {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String menu;
		
		System.out.println("Hello, it's StarCafe");	
		menu = scan.next();
		
		System.out.println("Ordered menu is : " + menu);
	}
}

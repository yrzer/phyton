using System;
public class Program{
	public static void Main(){
        Console.WriteLine("podaj lvl:");
        double lvl = Convert.ToInt32(Console.ReadLine()),xp_r=Math.Ceiling(60*Math.Pow(lvl , 2.8)-60),str;
		Console.WriteLine("lvl: "+lvl+"\nxp required: "+xp_r);
        Console.WriteLine("zapis do pliku...");
        string txt="";
        for (int i = 1; i < 1000; i++) {
        str = Math.Ceiling(60*Math.Pow(i , 2.8)-60);
        txt+="lvl-"+i+" xp required: "+ str.ToString() + "\n";
        }
        string path = @"C:\Users\GrzeSzcze\Documents\GitHub\phyton\C#\MyTest.txt";
        File.WriteAllTextAsync(path, txt);
        Console.WriteLine("już");
        Console.ReadKey();
	}
}
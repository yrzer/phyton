class zwierzenta {
    public String gatunek;
    public String imie;
    public int lata;
    public double waga;
 
    public zwierzenta(String imie,int lata, int waga, String gatunek) {
        this.lata = lata;
        this.waga = waga;
        this.gatunek = gatunek;
        this.imie = imie;
    }
    public void humor(){
      System.out.println("joloooooo!");
    }
}
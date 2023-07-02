package model;

public class Profit {
    private int count; // количество проданных игрушек
    private double price;// общая сумма

    public Profit(int count, double price) {
        this.count = count;
        this.price = price;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "всего " + count +
                ", игрушки(-ек) на сумму: " + price;
    }

}

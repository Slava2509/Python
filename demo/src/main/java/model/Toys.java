package model;

public class Toys {
    private long id;
    private String title;// название игрушки
    private String manufacturer; // производитель игрушки
    private double price; // цена
    private String gamesgroup;// группа игрушек
    private int quantity; // количество
    private double frequency; // частота покупки игрушки

    public Toys(long id, String title, String manufacturer, double price, String gamesgroup, int quantity) {
        this.id = id;
        this.title = title;
        this.manufacturer = manufacturer;
        this.price = price;
        this.gamesgroup = gamesgroup;
        this.quantity = quantity;
        this.frequency = frequency;
        }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public String getGamesgroup() {
        return gamesgroup;
    }

    public void setGamesgroup(String gamesgroup) {
        this.gamesgroup = gamesgroup;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getFrequency() {
        return frequency;
    }

    public void setFrequency(double frequency) {
        this.frequency = frequency;
    }
}

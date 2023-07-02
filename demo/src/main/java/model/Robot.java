package model;

public class Robot extends Toys {
    @Override
    public long getId() {
        return super.getId();
    }

    @Override
    public void setId(long id) {
        super.setId(id);
    }

    @Override
    public String getTitle() {
        return super.getTitle();
    }

    @Override
    public void setTitle(String title) {
        super.setTitle(title);
    }

    @Override
    public String getManufacturer() {
        return super.getManufacturer();
    }

    @Override
    public void setManufacturer(String manufacturer) {
        super.setManufacturer(manufacturer);
    }

    @Override
    public double getPrice() {
        return super.getPrice();
    }

    @Override
    public void setPrice(double price) {
        super.setPrice(price);
    }

    @Override
    public String getGamesgroup() {
        return super.getGamesgroup();
    }

    @Override
    public void setGamesgroup(String gamesgroup) {
        super.setGamesgroup(gamesgroup);
    }

    @Override
    public int getQuantity() {
        return super.getQuantity();
    }

    @Override
    public void setQuantity(int quantity) {
        super.setQuantity(quantity);
    }

    @Override
    public double getFrequency() {
        return super.getFrequency();
    }

    @Override
    public void setFrequency(double frequency) {
        super.setFrequency(frequency);
    }

    public Robot(long id, String title, String manufacturer, double price, String gamesgroup, int quantity) {
        super(id, title, manufacturer, price, gamesgroup, quantity);
    }
}

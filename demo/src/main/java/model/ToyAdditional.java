package model;

public class ToyAdditional {
    private ToyGroup gamesgroup;
    private int count;


    public ToyGroup getGamesgroup() {
        return gamesgroup;
    }

    public void setGamesgroup(ToyGroup gamesgroup) {
        this.gamesgroup = gamesgroup;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public ToyAdditional(ToyGroup gamesgroup, int count) {
        this.gamesgroup = gamesgroup;
        this.count = count;
    }
}

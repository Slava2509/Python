package com.example.demo;

import model.*;

import java.util.ArrayList;
import java.util.HashMap;

public class Main {
    static ArrayList<Toys> toys = new ArrayList<>();
    static ArrayList<Customer> customers = new ArrayList<>();
    static ArrayList<Employee> employees = new ArrayList<>();
    static ArrayList<Order> orders = new ArrayList<>();

    public static void main(String[] args) {
            initData();
        String toysInfo = String.format("Общее количество проданных игрушек %d на сумму %f",
                getCountOfSoldToys(),getAllPriceOfSoldToys());
        System.out.println(toysInfo);

        for (Employee employee : employees) {
            System.out.println(employee.getName() + " продал " + getProfitByEmployee(employee.getId()).toString());
        }

        ArrayList<ToyAdditional> soldToyCount = getCountOfSoldToysGamesgroup ();
        HashMap<ToyGroup, Double> soldToyPrices = getPriceOfSoldToysGamesgroup();
        String soldToyStr = "По виду игрушек: %s продано игрушек %d общей стоимостью %f";
        for (ToyAdditional toyAdditional :soldToyCount) {
            double price = soldToyPrices.get(toyAdditional.getGamesgroup());
            System.out.println(String.format(
                    soldToyStr,toyAdditional.getGamesgroup().name(),toyAdditional.getCount(),price));
        }
    }
    //получить количетсво игрушек в заказе по определенной группе товаров
    public static ArrayList <ToyAdditional> getCountOfSoldToysGamesgroup(){
        ArrayList <ToyAdditional> result = new ArrayList<>();
        int countRob = 0;
        int countCar = 0;
        int countDol = 0;
        for (Order order : orders) {
            countRob += getCountOfSoldToysGamesgroup(order, ToyGroup.Robots);
            countCar += getCountOfSoldToysGamesgroup(order, ToyGroup.Cars);
            countDol += getCountOfSoldToysGamesgroup(order, ToyGroup.Dolls);
        }
        result.add(new ToyAdditional(ToyGroup.Robots,countRob));
        result.add(new ToyAdditional(ToyGroup.Cars,countCar));
        result.add(new ToyAdditional(ToyGroup.Dolls,countDol));

        return result;
    }


    //получить количетсво игрушек в заказе по определенной группе товаров

    private static double getCountOfSoldToysGamesgroup(Order order, ToyGroup gamesgroup) {
        int count = 0;
        for (long toysId : order.getToys()) {
            Toys toys = getToyById(toysId);
            if (toys != null && toys.getGamesgroup() == gamesgroup.name()) {
                count++;
            }
        }
        return count;
    }


    //получить стоимость проданных игрушек по группе товаров

    public static HashMap<ToyGroup,Double> getPriceOfSoldToysGamesgroup (){
        HashMap<ToyGroup,Double> result = new HashMap<>();
        double priceRob = 0;
        double priceCar = 0;
        double priceDol = 0;
        for (Order order: orders) {
            priceRob += getPriceOfSoldToysGamesgroup(order, ToyGroup.Robots);
            priceCar += getPriceOfSoldToysGamesgroup(order, ToyGroup.Cars);
            priceDol += getPriceOfSoldToysGamesgroup(order, ToyGroup.Dolls);
        }
        result.put(ToyGroup.Robots,priceRob);
        result.put(ToyGroup.Cars,priceCar);
        result.put(ToyGroup.Dolls, priceDol);

        return result;

    }
    // получение общей суммы стоимости игрушек в одном заказе по группе игрушек
    private static double getPriceOfSoldToysGamesgroup(Order order, ToyGroup gamesgroup) {
        double price = 0;
        for (long toysId : order.getToys()) {
            Toys toys = getToyById(toysId);
            if (toys != null && toys.getGamesgroup() == gamesgroup.name()) {
                price += toys.getPrice();
            }
        }
        return price;
    }

    // получение общего количества и стоимости товара для конкретного продавца
    public static Profit getProfitByEmployee (long employeeId) {
        int count = 0;
        double price = 0;
        for (Order order: orders) {
            if (order.getEmployeeId() == employeeId) {
               price +=getPriceOfSoldToysInOrder(order);
               count += order.getToys().length;
            }
        }
        return new Profit(count, price);
    }

    // получение общей стоимости заказов
    public static double getAllPriceOfSoldToys () {
        double price = 0;
        for (Order order : orders) {
            price += getPriceOfSoldToysInOrder(order);
        }
        return price;
    }
    // получение общей стоимости одного заказа
    public static double getPriceOfSoldToysInOrder (Order order) {
        double price = 0;
        for (long toysId : order.getToys()) {
            Toys toys = getToyById(toysId);
            if (toys != null)
            price +=toys.getPrice();
        }
        return price;
    }
    // получение общего количества проданных игрушек
    public static int getCountOfSoldToys () {
        int count = 0;
        for (Order order: orders) {
            count += order.getToys().length;
        }
        return count;
    }
    // поиск игрушки по ее ID номеру
    public static Toys getToyById(long id) {
        Toys current = null;
        for (Toys toy : toys) {
            if (toy.getId() == id) {
               current = toy;
               break;
            }
        }
            return current;
    }

    public static void initData() {
        //продавцы
        employees.add(new Employee(1, "Иванов Иван", 21));
        employees.add(new Employee(2, "Петров Петр", 23));
        employees.add(new Employee(3, "Сидоров Сидр", 25));
        // покупатели
        customers.add(new Customer(1, "Васильев Вася", 35));
        customers.add(new Customer(2, "Медведев Вася", 26));
        customers.add(new Customer(3, "Лыкосова Ирина", 38));
        //игрушки
        toys.add(new Toys(1, "джип", "Porshe", 1000, "cars", 1));
        toys.add(new Toys(2, "спорткар", "Ferrari", 2000, "cars", 2));
        toys.add(new Toys(3, "грузовик", "Man", 1500, "cars", 3));
        toys.add(new Toys(4, "Оптимус", "Warner", 4000, "robots", 4));
        toys.add(new Toys(5, "Терминатор", "Scynet", 3000, "robots", 5));
        toys.add(new Toys(6, "Барби", "Barbie", 2500, "dolls", 6));
        //заказы
        orders.add(new Order(1, 2, 3, new long[]{5, 6}));
        orders.add(new Order(2, 3, 1, new long[]{1, 2}));
        orders.add(new Order(3, 1, 2, new long[]{3, 4, 6, 1}));
    }

}

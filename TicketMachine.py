import math
import time
import copy
from abc import ABCMeta, abstractmethod


class Prototyp:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(
                f'Incorrect object identifier: {identifier}')
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


class Ticket(metaclass=ABCMeta):
    def __str__(self):
        return 'Bilet'

    @abstractmethod
    def nazwa(self):
        pass

    @abstractmethod
    def cena(self):
        pass


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TicketKids(Ticket):
    price = 2

    def __init__(self):
        self.name = 'Bilet ulgowy'
        self.price = 2

    def __str__(self):
        return self.name

    def nazwa(self):
        return self.name

    def cena(self):
        return self.price


class TicketAdults(Ticket):
    price = 4

    def __init__(self):
        self.name = 'Bilet normalny'
        self.price = 4

    def __str__(self):
        return self.name

    def nazwa(self):
        return self.name

    def cena(self):
        return self.price


class CountCoinsAndNotes:
    def __init__(self):
        self.coins_20 = 0
        self.coins_50 = 0
        self.coins_1 = 0
        self.coins_2 = 0
        self.coins_5 = 0
        self.notes_10 = 0
        self.notes_20 = 0
        self.notes_50 = 0
        self.notes_100 = 0
        self.notes_200 = 0

    def toss_coins_20(self):
        self.coins_20 = input(f"How many 0.2$ coins do you want to toss?")

    def toss_coins_50(self):
        self.coins_50 = input(f"How many 0.5$ coins do you want to toss?")

    def toss_coins_1(self):
        self.coins_1 = input(f"How many 1$ coins do you want to toss?")

    def toss_coins_2(self):
        self.coins_2 = input(f"How many 2$ coins do you want to toss?")

    def toss_coins_5(self):
        self.coins_5 = input(f"How many 5$ coins do you want to toss?")

    def insert_notes_10(self):
        self.notes_10 = input(f"How many 10$ do you want to insert?")

    def insert_notes_20(self):
        self.notes_20 = input(f"How many 20$ do you want to insert?")

    def insert_notes_50(self):
        self.notes_50 = input(f"How many 50$ do you want to insert?")

    def insert_notes_100(self):
        self.notes_100 = input(f"How many 100$ do you want to insert?")

    def insert_notes_200(self):
        self.notes_200 = input(f"How many 200$ do you want to insert?")


class PayForTickets:

    def __init__(self, ticket_machine, amount_kids, amount_adults):
        print(f'Overall cost is: {self.calculate_cost(amount_kids, amount_adults)}')
        count = CountCoinsAndNotes()
        self.calculate_inserted_money(count)
        self.give_change(ticket_machine, count, amount_kids, amount_adults)

    def calculate_cost(self, number_of_kids, number_of_adults):
        kids_tickets = number_of_kids
        adults_tickets = number_of_adults
        kids_cost = kids_tickets * TicketKids.price
        adult_cost = adults_tickets * TicketAdults.price
        cost = kids_cost + adult_cost
        return cost

    def calculate_inserted_money(self, count_coins):
        count_coins.toss_coins_20()
        count_coins.toss_coins_50()
        count_coins.toss_coins_1()
        count_coins.toss_coins_2()
        count_coins.toss_coins_5()
        count_coins.insert_notes_10()
        count_coins.insert_notes_20()
        count_coins.insert_notes_50()
        count_coins.insert_notes_100()
        count_coins.insert_notes_200()

    def count_money(self, count_coins):
        money = int(count_coins.coins_20) * 0.2 + int(count_coins.coins_50) * 0.5 + int(count_coins.coins_1) + \
                int(count_coins.coins_2) * 2 + int(count_coins.coins_5) * 5 + int(count_coins.notes_10) * 10 + \
                int(count_coins.notes_20) * 20 + int(count_coins.notes_50) * 50 + int(count_coins.notes_100) * 100 + \
                int(count_coins.notes_200) * 200
        # print(f'Money w count : {money}')
        # print(f' Money po zamianie na int: {int(money)}')
        return money

    def is_enough_money(self, count_coins, number_of_kids, number_of_adults):
        cost = self.calculate_cost(number_of_kids, number_of_adults)
        money = self.count_money(count_coins)
        # print(f'koszt w is_enough_money {cost}')
        # print(f'hajs w is_enough_money {money}')
        if int(money) < cost:
            return False
        else:
            return True

    def check_amount(self, count_coins, number_of_kids, number_of_adults):
        if not self.is_enough_money(count_coins, number_of_kids, number_of_adults):
            print('You have inserted not enough money. Your money will now be ejected.')
            exit()

    def add_given_money(self, ticket_machine, count_coins):
        if int(count_coins.notes_200) >= 1:
            # print(f'liczba banknotow 200 przed dodaniem: {ticket_machine.amountOfNote200}')
            ticket_machine.amountOfNote200 += int(count_coins.notes_200)
        # print(f'Liczba banknotow 200 po dodaniu: {ticket_machine.amountOfNote200}')
        if int(count_coins.notes_100) >= 1:
            #     print(f'liczba banknotow 100 przed dodaniem: {ticket_machine.amountOfNote100}')
            ticket_machine.amountOfNote100 += int(count_coins.notes_100)
        #     print(f'Liczba banknotow 200 po dodaniu: {ticket_machine.amountOfNote200}')
        if int(count_coins.notes_50) >= 1:
            #   print(f'liczba banknotow 200 przed dodaniem: {ticket_machine.amountOfNote50}')
            ticket_machine.amountOfNote50 += int(count_coins.notes_50)
        #    print(f'Liczba banknotow 50 po dodaniu: {ticket_machine.amountOfNote50}')
        if int(count_coins.notes_20) >= 1:
            #   print(f'liczba banknotow 20 przed dodaniem: {ticket_machine.amountOfNote20}')
            ticket_machine.amountOfNote20 += int(count_coins.notes_20)
        #   print(f'Liczba banknotow 20 po dodaniu: {ticket_machine.amountOfNote20}')
        if int(count_coins.notes_10) >= 1:
            #    print(f'liczba banknotow 10 przed dodaniem: {ticket_machine.amountOfNote10}')
            ticket_machine.amountOfNote10 += int(count_coins.notes_10)
        #    print(f'Liczba banknotow 10 po dodaniu: {ticket_machine.amountOfNote10}')
        if int(count_coins.coins_5) >= 1:
            #    print(f'liczba monet 5 przed dodaniem: {ticket_machine.amountOfCoin5}')
            ticket_machine.amountOfCoin5 += int(count_coins.coins_5)
        #   print(f'Liczba monet 5 po dodaniu: {ticket_machine.amountOfCoin5}')
        if int(count_coins.coins_2) >= 1:
            #    print(f'liczba monet 2 przed dodaniem: {ticket_machine.amountOfCoin2}')
            ticket_machine.amountOfCoin2 += int(count_coins.coins_2)
        #    print(f'Liczba monet 2 po dodaniu: {ticket_machine.amountOfCoin2}')
        if int(count_coins.coins_1) >= 1:
            #    print(f'liczba monet 1 przed dodaniem: {ticket_machine.amountOfCoin1}')
            ticket_machine.amountOfCoin1 += int(count_coins.coins_1)
        #   print(f'Liczba monet 1 po dodaniu: {ticket_machine.amountOfCoin1}')
        if int(count_coins.coins_50) >= 1:
            #    print(f'liczba monet 0.50 przed dodaniem: {ticket_machine.amountOfCoin50}')
            ticket_machine.amountOfCoin50 += int(count_coins.coins_50)
        #   print(f'Liczba monet 0.5 po dodaniu: {ticket_machine.amountOfCoin50}')
        if int(count_coins.coins_20) >= 1:
            #    print(f'liczba monet 0.20 przed dodaniem: {ticket_machine.amountOfCoin20}')
            ticket_machine.amountOfCoin20 += int(count_coins.coins_20)
        #    print(f'Liczba monet 0.20 po dodaniu: {ticket_machine.amountOfCoin20}')

    def give_change(self, ticket_machine, count_coins, number_of_kids, number_of_adults):
        self.check_amount(count_coins, number_of_kids, number_of_adults)
        rest = self.count_money(count_coins) - self.calculate_cost(number_of_kids, number_of_adults)
        if rest == 0:
            print('You have inserted the exact amount of money needed. Now the tickets will be printed.')
            time.sleep(3)
            print(f'Thank you! Have a nice day!')
            exit()
        # print(f' Reszta w giveChange: {rest}')
        two_hundreds = 0
        one_hundreds = 0
        fifties = 0
        twenties = 0
        tens = 0
        fives = 0
        twos = 0
        ones = 0
        fifty_cents = 0
        twenty_cents = 0
        if rest >= 200:
            if ticket_machine.amountOfNote200 > math.floor(rest / 200):
                two_hundreds = math.floor(rest / 200)
                rest -= two_hundreds * 200
                ticket_machine.amountOfNote200 -= two_hundreds
            #    print(f'reszta = {rest}')
            #    print(f'ilosc banknotow 200: {ticket_machine.amountOfNote200}')
        if rest >= 100:
            if ticket_machine.amountOfNote100 > math.floor(rest / 100):
                one_hundreds = math.floor(rest / 100)
                rest -= one_hundreds * 100
                ticket_machine.amountOfNote100 -= one_hundreds
            #    print(f'reszta = {rest}')
            #    print(f'ilosc banknotow 100: {ticket_machine.amountOfNote100}')
        if rest >= 50:
            if ticket_machine.amountOfNote50 > math.floor(rest / 50):
                fifties = math.floor(rest / 50)
                rest -= fifties * 50
                ticket_machine.amountOfNote50 -= fifties
            #   print(f'reszta = {rest}')
            #   print(f'ilosc banknotow 50: {ticket_machine.amountOfNote50}')
        if rest >= 20:
            if ticket_machine.amountOfNote20 > math.floor(rest / 20):
                twenties = math.floor(rest / 20)
                rest -= twenties * 20
                ticket_machine.amountOfNote20 -= twenties
            #    print(f'reszta = {rest}')
            #    print(f'ilosc banknotow 20: {ticket_machine.amountOfNote20}')
        if rest >= 10:
            if ticket_machine.amountOfNote10 > math.floor(rest / 10):
                tens = math.floor(rest / 10)
                rest -= tens * 10
                ticket_machine.amountOfNote10 -= tens
            #    print(f'reszta = {rest}')
            #   print(f'ilosc banknotow 10: {ticket_machine.amountOfNote10}')
        if rest >= 5:
            if ticket_machine.amountOfCoin5 > math.floor(rest / 5):
                fives = math.floor(rest / 5)
                rest -= fives * 5
                ticket_machine.amountOfCoin5 -= fives
            #  print(f'reszta = {rest}')
            #  print(f'ilosc monet 5: {ticket_machine.amountOfCoin5}')
        if rest >= 2:
            if ticket_machine.amountOfCoin2 > math.floor(rest / 2):
                twos = math.floor(rest / 2)
                rest -= twos * 2
                ticket_machine.amountOfCoin2 -= twos
            #   print(f'reszta = {rest}')
            #  print(f'ilosc monet 2: {ticket_machine.amountOfCoin2}')
        if rest >= 1:
            if ticket_machine.amountOfCoin1 > math.floor(rest / 1):
                ones = math.floor(rest / 1)
                rest -= ones * 1
                ticket_machine.amountOfCoin1 -= ones
            #   print(f'reszta = {rest}')
            #   print(f'ilosc monet 1: {ticket_machine.amountOfCoin1}')
        if rest >= 0.5:
            if ticket_machine.amountOfCoin50 > math.floor(rest / 0.5):
                fifty_cents = math.floor(rest / 0.5)
                rest -= fifty_cents * 0.5
                ticket_machine.amountOfCoin50 -= fifty_cents
            #   print(f'reszta = {rest}')
            #   print(f'ilosc monet 0.5: {ticket_machine.amountOfCoin50}')
        if rest >= 0.2:
            if ticket_machine.amountOfCoin20 > math.floor(rest / 0.2):
                twenty_cents = math.floor(rest / 0.2)
                rest -= twenty_cents * 0.2
                ticket_machine.amountOfCoin20 -= twenty_cents
            #   print(f'reszta = {rest}')
            #   print(f'ilosc monet 0.20: {ticket_machine.amountOfCoin20}')
        if rest > 0:
            print(f'Sorry, there is not enough notes and/or coins to give change. Please insert exact amount of money.')
        else:
            print(f'The tickets are being printed.')
            time.sleep(5)
            print(f'Giving change: {two_hundreds} x 200$, {one_hundreds} x 100$, {fifties} x 50$, {twenties} x 20$,'
                  f' {tens} x 10$, {fives} x 5$, {twos} x 2$, {ones} x 1$, {fifty_cents}x 0.5 $, {twenty_cents} x 0.2$')
            time.sleep(3)
            self.add_given_money(ticket_machine, count_coins)
            print(f'Thank you! Have a nice day!')


class TicketMachine(metaclass=SingletonType):
    def __init__(self):
        print(f'Initiating machine...')
        self.amountOfCoin20 = None
        self.amountOfCoin50 = None
        self.amountOfCoin1 = None
        self.amountOfCoin2 = None
        self.amountOfCoin5 = None
        self.amountOfNote10 = None
        self.amountOfNote20 = None
        self.amountOfNote50 = None
        self.amountOfNote100 = None
        self.amountOfNote200 = None


class TicketMachineBuilder:
    def __init__(self):
        print(f'Building machine...')
        self.TicketMachine = TicketMachine()

    def refill_coin_20(self, amount):
        self.TicketMachine.amountOfCoin20 = amount

    def refill_coin_50(self, amount):
        self.TicketMachine.amountOfCoin50 = amount

    def refill_coin_1(self, amount):
        self.TicketMachine.amountOfCoin1 = amount

    def refill_coin_2(self, amount):
        self.TicketMachine.amountOfCoin2 = amount

    def refill_coin_5(self, amount):
        self.TicketMachine.amountOfCoin5 = amount

    def refill_note_10(self, amount):
        self.TicketMachine.amountOfNote10 = amount

    def refill_note_20(self, amount):
        self.TicketMachine.amountOfNote20 = amount

    def refill_note_50(self, amount):
        self.TicketMachine.amountOfNote50 = amount

    def refill_note_100(self, amount):
        self.TicketMachine.amountOfNote100 = amount

    def refill_note_200(self, amount):
        self.TicketMachine.amountOfNote200 = amount


class TicketMachineOperator:
    def __init__(self):
        self.builder = None

    def construct_ticket_machine(self):
        self.builder = TicketMachineBuilder()   #domyslnie jest 2340 zl
        self.builder.refill_coin_20(100)
        self.builder.refill_coin_50(100)
        self.builder.refill_coin_1(200)
        self.builder.refill_coin_2(200)
        self.builder.refill_coin_5(50)
        self.builder.refill_note_10(20)
        self.builder.refill_note_20(15)
        self.builder.refill_note_50(10)
        self.builder.refill_note_100(5)
        self.builder.refill_note_200(3)

    @property
    def ticket_machine(self):
        return self.builder.TicketMachine


def main():
    ticket_machine_operator = TicketMachineOperator()
    ticket_machine_operator.construct_ticket_machine()
    ticket_machine = ticket_machine_operator.ticket_machine
    print('Welcome to TicketMaster 2077!')
    amount_adults = int(input("How many Adults tickets do you want to buy? "))
    if int(amount_adults) > 0:
        a = TicketAdults()
        adults_tickets = []
        prototype_adults = Prototyp()
        identifier = 'Adults'
        prototype_adults.register(identifier, a)
        for i in range(1, amount_adults):
            adults_tickets.append(prototype_adults.clone(identifier))
    amount_kids = int(input("How many Kids tickets do you want to buy? "))
    if int(amount_kids) > 0:
        k = TicketKids()
        kids_tickets = []
        prototype_kids = Prototyp()
        identifier = 'Kids'
        prototype_kids.register(identifier, k)
        for i in range(1, amount_kids):
            kids_tickets.append(prototype_kids.clone(identifier))
    PayForTickets(ticket_machine, amount_kids, amount_adults)


if __name__ == '__main__':
    main()

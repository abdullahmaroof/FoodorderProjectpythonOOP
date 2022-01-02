from random import *

class for_bill:
    rand_value = randint(1000, 4000)
    food = ""
    flavour = ""
    size = ""
    servewith = ""
    price = ""
    note = ""


class spizza_chf(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Chicken Fajita"
    size = "Small 5\""
    price = 300
    note = "Your order will be serve in 20 min. Thank you!!!"

class mpizza_chf(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Chicken Fajita"
    size = "Medium 8\""
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"

class lpizza_chf(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Chicken Fajita"
    size = "Large 13\""
    price = 800
    note = "Your order will be serve in 20 min. Thank you!!!"

class spizza_peeri(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Peeri Peeri"
    size = "Small 5\""
    price = 350
    note = "Your order will be serve in 20 min. Thank you!!!"

class mpizza_peeri(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Peeri Peeri"
    size = "Medium 8\""
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"

class lpizza_peeri(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Smoke Mexico"
    size = "Large 13\""
    price = 900
    note = "Your order will be serve in 20 min. Thank you!!!"


class spizza_m(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Smoke Mexico"
    size = "Small 5\""
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"

class mpizza_m(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Smoke Mexico"
    size = "Medium 8\""
    price = 800
    note = "Your order will be serve in 20 min. Thank you!!!"

class lpizza_m(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Smoke Mexico"
    size = "Large 13\""
    price = 1100
    note = "Your order will be serve in 20 min. Thank you!!!"

class spizza_ch(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Cheese"
    size = "Small 5\""
    price = 320
    note = "Your order will be serve in 20 min. Thank you!!!"

class mpizza_ch(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Cheese"
    size = "Medium 8\""
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"

class lpizza_ch(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Cheese"
    size = "Large 13\""
    price = 950
    note = "Your order will be serve in 20 min. Thank you!!!"

class spizza_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Bar BQ"
    size = "Small 5\""
    price = 350
    note = "Your order will be serve in 20 min. Thank you!!!"

class mpizza_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Bar BQ"
    size = "Medium 8\""
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"

class lpizza_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Pizza"
    flavour = "Bar BQ"
    size = "Large 13\""
    price = 1000
    note = "Your order will be serve in 20 min. Thank you!!!"

class burger_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Zinger"
    servewith = "none"
    price = 400
    note = "Your order will be serve in 20 min. Thank you!!!"

class dburger_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Zinger"
    servewith = "Drink"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"

class fburger_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Zinger"
    servewith = "Fries"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class burger_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Beef"
    servewith = "none"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"


class dburger_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Beef"
    servewith = "Drink"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class fburger_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Beef"
    servewith = "Fries"
    price = 700
    note = "Your order will be serve in 20 min. Thank you!!!"


class burger_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Chicken"
    servewith = "none"
    price = 450
    note = "Your order will be serve in 20 min. Thank you!!!"


class dburger_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Chicken"
    servewith = "Drink"
    price = 550
    note = "Your order will be serve in 20 min. Thank you!!!"


class fburger_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Chicken"
    servewith = "Fries"
    price = 650
    note = "Your order will be serve in 20 min. Thank you!!!"


class burger_shotgun(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Shotgun"
    servewith = "none"
    price = 350
    note = "Your order will be serve in 20 min. Thank you!!!"


class dburger_shotgun(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Shotgun"
    servewith = "Drink"
    price = 450
    note = "Your order will be serve in 20 min. Thank you!!!"


class fburger_shotgun(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Shotgun"
    servewith = "Fries"
    price = 550
    note = "Your order will be serve in 20 min. Thank you!!!"

class burger_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Bar BQ"
    servewith = "none"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"


class dburger_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Bar BQ"
    servewith = "Drink"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class fburger_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Burger"
    flavour = "Bar BQ"
    servewith = "Fries"
    price = 700
    note = "Your order will be serve in 20 min. Thank you!!!"

class parroll_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Zinger"
    servewith = "none"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"

class dparroll_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Zinger"
    servewith = "Drink"
    price = 550
    note = "Your order will be serve in 20 min. Thank you!!!"

class fparroll_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Zinger"
    servewith = "Fries"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class parroll_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Beef"
    servewith = "none"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class dparroll_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Beef"
    servewith = "Drink"
    price = 650
    note = "Your order will be serve in 20 min. Thank you!!!"


class fparroll_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Beef"
    servewith = "Fries"
    price = 700
    note = "Your order will be serve in 20 min. Thank you!!!"


class parroll_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Chicken"
    servewith = "none"
    price = 450
    note = "Your order will be serve in 20 min. Thank you!!!"


class dparroll_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Chicken"
    servewith = "Drink"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"


class fparroll_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Chicken"
    servewith = "Fries"
    price = 550
    note = "Your order will be serve in 20 min. Thank you!!!"


class parroll_smoke(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Smoke"
    servewith = "none"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class dparroll_smoke(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Smoke"
    servewith = "Drink"
    price = 650
    note = "Your order will be serve in 20 min. Thank you!!!"


class fparroll_smoke(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Smoke"
    servewith = "Fries"
    price = 700
    note = "Your order will be serve in 20 min. Thank you!!!"

class parroll_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Bar BQ"
    servewith = "none"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"


class dparroll_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Bar BQ"
    servewith = "Drink"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class fparroll_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Paratha Roll"
    flavour = "Bar BQ"
    servewith = "Fries"
    price = 700
    note = "Your order will be serve in 20 min. Thank you!!!"

class biryani_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Zinger"
    servewith = "none"
    price = 300
    note = "Your order will be serve in 20 min. Thank you!!!"

class dbiryani_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Zinger"
    servewith = "Drink"
    price = 350
    note = "Your order will be serve in 20 min. Thank you!!!"

class fbiryani_zinger(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Zinger"
    servewith = "Salad"
    price = 400
    note = "Your order will be serve in 20 min. Thank you!!!"


class biryani_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Beef"
    servewith = "none"
    price = 500
    note = "Your order will be serve in 20 min. Thank you!!!"


class dbiryani_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Beef"
    servewith = "Drink"
    price = 550
    note = "Your order will be serve in 20 min. Thank you!!!"


class fbiryani_beef(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Beef"
    servewith = "Salad"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class biryani_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Chicken"
    servewith = "none"
    price = 250
    note = "Your order will be serve in 20 min. Thank you!!!"


class dbiryani_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Chicken"
    servewith = "Drink"
    price = 300
    note = "Your order will be serve in 20 min. Thank you!!!"


class fbiryani_chicken(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Chicken"
    servewith = "Salad"
    price = 350
    note = "Your order will be serve in 20 min. Thank you!!!"


class biryani_Chrice(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Chinese Rice"
    servewith = "none"
    price = 200
    note = "Your order will be serve in 20 min. Thank you!!!"


class dbiryani_Chrice(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Chinese Rice"
    servewith = "Drink"
    price = 250
    note = "Your order will be serve in 20 min. Thank you!!!"


class fbiryani_Chrice(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Chinese Rice"
    servewith = "Salad"
    price = 300
    note = "Your order will be serve in 20 min. Thank you!!!"

class biryani_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Bar BQ"
    servewith = "none"
    price = 600
    note = "Your order will be serve in 20 min. Thank you!!!"


class dbiryani_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Bar BQ"
    servewith = "Drink"
    price = 650
    note = "Your order will be serve in 20 min. Thank you!!!"


class fbiryani_bbq(for_bill):
    rand_value = randint(1000, 4000)
    food = "Biryani"
    flavour = "Bar BQ"
    servewith = "Salad"
    price = 700
    note = "Your order will be serve in 20 min. Thank you!!!"
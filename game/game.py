import datetime
import pickle
import random as r
import os
import time


class Char:

    def __init__(self, name, probability):
        self._name = name
        self._number = probability
        self._day = 1
        self._dialog = []

    def get_probability(self):
        return self._number

    def get_name(self):
        return self._name


def initialize():
    try:
        with open('savefile.txt', 'rb') as f:
            data = pickle.load(f)
            print("Data loaded.")
            return data
    except IOError:
        data = {"date": datetime.date.today().strftime("%m/%d/%Y"),
                "days": 0, "c_dane": 0, "c_ellie": 0, "c_westra": 0,
                "c_ember": 0, "c_dane_ellie": 0, "inventory": []}
        return data


def find_day(data):
    current_day = datetime.date.today().strftime("%m/%d/%Y")
    print("The current day is: " + str(current_day))
    day = data["date"]
    if day == current_day and data['days'] != 0:
        add_day = False
        return add_day
    else:
        add_day = True
        data["days"] += 1
        data["date"] = current_day
        return add_day


def who_here(data):
    """
    determines who is in the cafe today by rolling random integers
    :param data: The gamedata file.
    :return:
    """
    patrons = data['characters']
    if data["days"] >= 3:
        patrons.append(Char("Ellie", 9))
    if data["days"] >= 5:
        patrons.append(Char("Westra", 8))
    if data["days"] >= 7:
        patrons.append(Char("Ember", 7))
    in_cafe = []
    print(patrons)
    for indiv in patrons:
        prob = r.randint(0, 11)
        prob_pat = indiv.get_probability()
        if prob <= prob_pat:
            in_cafe.append(indiv.get_name())
            print(str(indiv.get_name()) + " is here today.")
        else:
            print(str(indiv.get_name()) + " is not here today.")
    if "Dane" in in_cafe and "Ellie" in in_cafe:
        if data["c_ellie"] >= 2:
            in_cafe.remove("Dane")
            in_cafe.remove("Ellie")
            in_cafe.append("Dane + Ellie")
        else:
            in_cafe.remove("Dane")
    data['in_cafe'] = in_cafe
    return in_cafe


def check_who(patron_list):
    who_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if "Dane" in patron_list:
        who_list[0] = 1
    else:
        who_list[0] = 0
    if "Ellie" in patron_list:
        who_list[1] = 1
    else:
        who_list[1] = 0
    if "Westra" in patron_list:
        who_list[2] = 1
    else:
        who_list[2] = 0
    if "Ember" in patron_list:
        who_list[3] = 1
    else:
        who_list[3] = 0
    if "Dane + Ellie" in patron_list:
        who_list[0] = 0
        who_list[1] = 0
        who_list[4] = 1
    return who_list

def where_who(who_list, data):
    if who_list[0] == 1:
        if data["c_dane"] >= 3:
            who_list[0] = 3

def on_quit(data):
    print("Saving...")
    with open('savefile.txt', 'wb') as save:
        pickle.dump(data, save)
    print("Save Completed.")


def delete_save():
    print("Thanks for stopping by.")
    print("Deleting..")
    os.remove("savefile.txt")
    print("Deleted.")

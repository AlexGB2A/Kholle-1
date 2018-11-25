#!/usr/bin/env python3

# Alexandre Garnier 25/11/18
# Utilitaire faisant des opération sur une listre d'entier sotckée au format csv

import sys
import csv

def Max_List():
    print("Max")

def Min_List():
    print("Min")

def Moy_List():
    print("Moy")

def Delete_All():
    print("Delete_all")
    file = open("test.csv", "r+")
    buffer = list(csv.reader(file))
    buffer[:] = []
    file.close()
    return (buffer)

def Desc_Sort():
    print("sorting descending")
    file = open("test.csv", "r+")
    buffer = list(map(csv.reader(file), file))
    reverse_sort = sorted(buffer, reverse=True)
    print(reverse_sort)
    file.close()
    return (reverse_sort)

def Asc_Sort():
    print ("sorting ascending")
    file = open("test.csv", "r+")
    buffer = csv.reader(file)
    sort = sorted(buffer)
    print(sort)
    file.close()
    return (sort)

def List_All():
    print("List_All")
    file = open("test.csv", "r+")
    buffer = csv.reader(file)
    print (list(buffer))
    file.close()
    return (buffer)

def Help_Msg():
    print("Description: Do operation on a list of integers sotcked on csv format")
    print("Usage:\t -c Delete all items on list")
    print("\t -l List all items on list")
    print("\t -t sorting ascending")
    print("\t -t --desc descending sort")
    print("\t -s --max List all items on list")
    print("\t -s --min List all items on list")
    print("\t -s --moy average of all items on list")


def choose_option():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "-c"):
            Delete_All()
        if (sys.argv[1] == "-l"):
            List_All()
        if (sys.argv[1] == "-t"):
            Asc_Sort()
        if (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            Help_Msg()
    elif (len(sys.argv) >= 3):
        if (sys.argv[1] == "-s" and sys.argv[2] == "--max"):
            Max_List()
        if (sys.argv[1] == "-s" and sys.argv[2] == "--min"):
            Min_List()
        if (sys.argv[1] == "-s" and sys.argv[2] == "--moy"):
            Moy_List()
        if (sys.argv[1] == "-t" and sys.argv[2] == "--desc"):
            Desc_Sort()

choose_option()

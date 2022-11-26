import csv
import os.path
import view

def find_surname(surname):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if surname == item[0]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'{surname} не найден!')
    else:
        view.answer('Файл не найден!')

def find_name(name):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if name == item[1]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с именем {find_name} не найден!')
    else:
        view.answer('Файл не найден!')

def find_name2(name2):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if name2 == item[2]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с  отчеством {find_name2} не найден!')
    else:
        view.answer('Файл не найден!')

def find_number_phone(number_phone):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if number_phone == item[3]:
                    view.answer(item)
                    count+=1
            if count == 0:
                view.answer(f'Человек с номером {number_phone} не найден!')
    else:
        view.answer('Файл не найден!')

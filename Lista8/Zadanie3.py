def positions():
    dict_pos_emp = {}
    dict_pos = {}
    with open("pracownicy.csv", encoding='utf-8') as pracownicy:
        for line in pracownicy:
            dict_pos_emp[line.strip().split(';')[2]] = line.strip().split(';')[3]


    with open("placowki.csv", encoding='utf-8') as placowki:
        for line in placowki:
            set_pos = set()
            employees = line.strip().split(';')[3:]
            for number in employees:
                set_pos.add(dict_pos_emp.get(number))
                dict_pos[line.strip().split(';')[0]] = set_pos

    return dict_pos
                

def branches_with(pos):
    branches = []
    positions_dict = positions()
    for key, value in positions_dict.items():
        if pos in value:
            branches.append(int(key))

    return branches


def year_emp():
    dict_emp_year = {}
    with open("pracownicy.csv", encoding='utf-8') as pracownicy:
        for line in pracownicy:
            dict_emp_year[line.strip().split(';')[2]] = line.strip().split(';')[4]

    return dict_emp_year



def old_employees():
    old_emp = []
    dict_emp_year = year_emp()
    with open("placowki.csv", encoding='utf-8') as placowki:
        for line in placowki:
            for employee in line.strip().split(';')[3:]:
                if  line.strip().split(';')[2] > dict_emp_year[employee]:
                    old_emp.append(employee)

    return sorted(old_emp) 

def cities():
    dict_city = {}
    with open("placowki.csv", encoding='utf-8') as placowki:
        for line in placowki:
            dict_city[int(line.strip().split(';')[0])] = line.strip().split(';')[1]

    return dict_city

def manager_cities():
    dict_city = cities()
    manager_cities_set = set()
    numbers_list = branches_with('manager')
    for number in numbers_list:
        manager_cities_set.add(dict_city[number])

    manager_cities_list = list(manager_cities_set)

    return sorted(manager_cities_list)



if __name__ == "__main__":
    print(positions())
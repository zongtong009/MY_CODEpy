import pickle
import os

datafile = 'person.data'
line = '''=======================================
press 1 to show list    ;   press 2 to add pepole
press 3 to edit pepole  ;   press 4 to delete pepole
press 5 to search pepole;   press 6 to show menu
press 0 to quit    '''
message = '''
=======================================
Welcome bookmark:
    press 1 to show list
    press 2 to add pepole
    press 3 to edit pepole
    press 4 to delete pepole
    press 5 to search pepole
    press 6 to show menu
    press 0 to quit
=======================================
'''
print(message)


class Person(object):
    """通讯录联系人"""

    def __init__(self, name, number):
        self.name = name
        self.number = number


def get_data(filename=datafile):  # 获取数据
    # 文件存在且不为空
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None


def set_data(name, number, filename=datafile):
    # 写入数据
    personList = {} if get_data() == None else get_data()

    with open(filename, 'wb') as f:
        personList[name] = Person(name, number)
        pickle.dump(personList, f)


def save_data(dictPerson, filename=datafile):
    # 保存字典格式的数据到文件
    with open(filename, 'wb') as f:
        pickle.dump(dictPerson, f)


def show_all():
    # 显示所有联系人
    personList = get_data()
    if personList:
        for v in personList.values():
            print(v.name, v.number)
        print(line)
    else:
        print('not yet person,please add person')
        print(line)


def add_person(name, number):
    # 添加联系人
    set_data(name, number)
    print('success add person')
    print(line)


def edit_person(name, number):
    # 编辑联系人
    personList = get_data()
    if personList:
        personList[name] = Person(name, number)
        save_data(personList)
        print('success edit person')
        print(line)


def delete_person(name):
    # 删除联系人
    personList = get_data()
    if personList:
        if name in personList:
            del personList[name]
            save_data(personList)
            print('success delete person')
        else:
            print(name, ' is not exists in dict')
        print(line)


def search_person(name):
    # 搜索联系人
    personList = get_data()
    if personList:
        if name in personList.keys():
            print(personList.get(name).name, personList.get(name).number)
        else:
            print('No this person of ', name)
        print(line)


while True:
    num = input('>>')

    if num == '1':
        print('show all personList:')
        show_all()
    elif num == '2':
        print('add person:')
        name = input('input name>>')
        number = input('input number>>')
        add_person(name, number)
    elif num == '3':
        print('edit person:')
        name = input('input name>>')
        number = input('input number>>')
        edit_person(name, number)
    elif num == '4':
        print('delete person:')
        name = input('input name>>')
        delete_person(name)
    elif num == '5':
        print('search :')
        name = input('input name>>')
        search_person(name)
    elif num == '6':
        print(message)
    elif num == '0':
        sure = input("Are you sure want to quit(y/n): ")
        if sure=="y":
            break
        else:
            print(line)
    else:
        print('input error, please retry')

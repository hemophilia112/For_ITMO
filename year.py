from datetime import datetime

names = ["Вася","Пётр","Александр","Влад"]
instrument_dict = {'name':"Дрель", 'quantity': 100, 'status': 'Есть свободные'}
organization_dict = {}



def app(name,organization, user_quantity, instrument):
    while True:
        if instrument_dict['quantity'] < 1:
            instrument_dict['status'] = 'Свободных нет'
            break
        if name in names:
            organization_dict['name'] = organization
            organization_dict['time'] = datetime.now()
            if instrument in instrument_dict['name']:
                if instrument_dict['status'] == "Есть свободные":
                    instrument_dict['quantity'] -= user_quantity
                    return f'Успех. Товара {instrument_dict['name']} осталось {instrument_dict['quantity']} шт.'
                else:
                    return f'Ошибка. Недостаточно товара на складе '
            else:
                return f'Ошибка. Товара {instrument} не найдено.'
        else:
            return f'Ошибка. Пользователя {name} не найдено в системе.'




print(app("Вася", "Какая-то организация", 20, "Дрель"))
print(organization_dict['name'], organization_dict['time'])









def persdata(name, surname, birthday, city, email, number):
    return (f'Имя - {name},'
            f' Фамилия - {surname},'
            f' Дата рождения - {birthday},'
            f' Город - {city},'
            f' email - {email},'
            f' number - {number}')

print(persdata(
    name = 'Привет',
    surname = 'Смирнов',
    birthday = '23.08.1993',
    city = 'Москва',
    email = 'example@mail.ru',
    number = '987 654 32 92'))
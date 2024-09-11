from faker import Faker


class RegistrationDate:
    @staticmethod
    def registration_courier_without_password():
        faker = Faker()
        login = faker.user_name()
        first_name = faker.name()
        data = {
            "login": login,
            "name": first_name
        }
        return data

    @staticmethod
    def registration_correct_courier():
        faker = Faker()
        login = faker.user_name()
        password = faker.password()
        first_name = faker.name()
        data = {
            "login": login,
            "password": password,
            "name": first_name
        }
        return data

    @staticmethod
    def registration_courier_without_login():
        faker = Faker()
        password = faker.password()
        first_name = faker.name()
        data = {
            "password": password,
            "name": first_name
        }
        return data

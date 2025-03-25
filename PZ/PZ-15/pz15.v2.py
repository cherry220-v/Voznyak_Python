class BankAccount:
    def __init__(self, client_id, full_name, periodic_payment, annual_rate, deposit_term, has_card):
        self.client_id = client_id
        self.full_name = full_name
        self.periodic_payment = periodic_payment
        self.annual_rate = annual_rate
        self.deposit_term = deposit_term
        self.has_card = has_card
        self.final_amount = self.calculate_final_amount()

    def calculate_final_amount(self):
        total = 0
        for _ in range(self.deposit_term * 12):
            total = (total + self.periodic_payment) * (1 + self.annual_rate / 12 / 100)
        return round(total, 2)

    def display_info(self):
        print(f"Код клиента: {self.client_id}")
        print(f"Ф.И.О.: {self.full_name}")
        print(f"Периодический платеж: {self.periodic_payment} руб.")
        print(f"Годовой процент: {self.annual_rate}%")
        print(f"Срок вклада: {self.deposit_term} лет")
        print(f"Пластиковая карта: {'Да' if self.has_card else 'Нет'}")
        print(f"Конечная сумма: {self.final_amount} руб.\n")


client1 = BankAccount(1, "Иванов Иван Иванович", 5000, 5, 3, True)
client2 = BankAccount(2, "Петров Петр Петрович", 10000, 7, 5, False)

client1.display_info()
client2.display_info()

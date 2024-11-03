class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget 

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        if category_name:
            self.__category_name = category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget

    def add_expense(self, amount):
        if 0 < amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
            print(f"Added expense of {amount} to {self.__category_name}.")
        else:
            print("Invalid expense amount or insufficient budget.")

    def display_category_summary(self):
        print(f"{self.__category_name} Budget: Allocated = {self.__allocated_budget}, Remaining = {self.__remaining_budget}")
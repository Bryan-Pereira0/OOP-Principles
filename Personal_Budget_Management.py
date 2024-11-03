from Budget_Category import BudgetCategory

def main():
    food = BudgetCategory("Food", 500)
    food.add_expense(100)
    food.display_category_summary()


main()
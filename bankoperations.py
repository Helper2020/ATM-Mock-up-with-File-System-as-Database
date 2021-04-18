import database


def deposit_operation(user):
    print("Deposit Operations")

    # get current balance
    current_balance = get_current_balance(user)

    # get amount to deposit
    bad_input = True
    while bad_input:
        try:
            amount = int(input("How much would you like to deposit?\n"))
            if amount < 1:
                print("Please enter a number greater than zero.")
            else:
                bad_input = False
        except ValueError:
            print('Please enter a number')

    # add deposited amount to current balance
    current_balance += amount

    # display current balance
    user[5] = str(amount)

    if database.update_balance(user):
        print('Current saving balance: %d' % current_balance)
    else:
        print('Deposit failed contact tech support')


def withdrawal_operation(user):
    print("withdrawal")

    # get current balance
    current_balance = get_current_balance(user)

    # get amount to withdraw
    bad_input = True
    while bad_input:
        try:
            amount = int(input("How much would you like to withdraw?\n"))
            bad_input = False
        except ValueError:
            print('Please enter a number')

    # check if current balance > withdraw balance
    if current_balance - amount < 0:
        print("Not enough funds")
        return
    else:
        # deduct withdrawn amount form current balance
        current_balance -= amount
        user[5] = str(current_balance)
        database.update_balance(user)
        # display current balance
        print('Current saving balance: %d' % current_balance)


def get_current_balance(user):
    return float(user[5])




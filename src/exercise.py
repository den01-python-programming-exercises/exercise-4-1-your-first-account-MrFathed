def main():
    #write your code below this line
    my_account = Account("My account", 100)
    my_account.deposit(20)

    print(my_account.balance)

# Don't edit below this line - this setup is required for testing
if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account

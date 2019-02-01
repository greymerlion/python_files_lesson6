# create a class of Wallet
# in wallet, there should be three features
# the wallet should have a self variable for coin count
# you should be able to initialize the wallet's coin count with a number, else it should default to 0
# the wallet should have a funtion/method give(x) - give x number of coins out of the wallet
# NOTE: a wallet cannot give out more than the coins it has, it should fail to give out and print an error
# the wallet should have a funtion/method  receive(x) -- receive x number of coins into the wallet
# NOTE: a wallet cannot store more than 100 coins, it should not accept the give and print an error
# print_amount() prints the current number of coins the wallet has 
# you must run the following tests on your wallet

my_wallet = Wallet(25)
my_wallet.give(10)
my_wallet.take(5)
my_wallet.give(20)
print(my_wallet.print_amount()) # answer should be 50

your_wallet = Wallet()
your_wallet.give(25)
your_wallet.give(100) # this should fail with a message
your_wallet.take(30)  # this should fail with a message
print(your_wallet.print_amount()) # answer should be 25

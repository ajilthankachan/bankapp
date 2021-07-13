class Bank:
    users = {
        1000: {'acc_num': 1000, 'password': 'ajil', 'salary': 150000},
        1001: {'acc_num': 1001, 'password': 'elna', 'salary': 250000},
        1002: {'acc_num': 1002, 'password': 'joann', 'salary': 350000},
        1003: {'acc_num': 1003, 'password': 'norah', 'salary': 400000},
        1004: {'acc_num': 1004, 'password': 'ashik', 'salary': 450000}
    }

    session = {}

    def validate_account(self, accno):
        if accno in self.users:
            return True
        else:
            return False

    def authenticate(self, **kwargs):  # kwargs = {acc_no:100, password="test"}
        acc_no = kwargs["acc_no"]
        password = kwargs["password"]
        user = self.validate_account(acc_no)

        if user:
            if password == self.users[acc_no]["password"]:
                self.session["user"] = acc_no
                return acc_no
            else:
                return -1
        else:
            return 0

    def get_salary(self, acc):
        if acc == self.session["user"]:
            salary = self.users[acc]["salary"]
            return salary
        else:
            print("you must login to perform a transaction.")

    def fund_transfer(self, user, to_user, amt):
        if self.validate_account(to_user):
            balance = self.get_salary(user)

            if balance > amt:
                self.users[user]["salary"] -= amt
                self.users[to_user]["salary"] += amt
            else:
                print("insufficient amount")

    def logout(self):
        self.session = 0


user1 = Bank()
logged_user = user1.authenticate(acc_no=1000, password="ajil")
# user1.get_salary(1003)
if logged_user == -1 or logged_user == 0:
    print("authentication failed")
else:
    print(f'hi {logged_user}, your bank balance is {user1.get_salary(logged_user)}')

user1.fund_transfer(logged_user, 1003, 100000)
print(f'hi {logged_user}, your bank balance after transfer is {user1.get_salary(logged_user)}')


logged_user1 = user1.authenticate(acc_no=1003, password="norah")
print(f'hi {logged_user1}, your bank balance is {user1.get_salary(logged_user1)}')
user1.logout()

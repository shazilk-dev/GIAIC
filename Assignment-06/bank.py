class Bank:
    bank_name = "National Bank"
    
    def __init__(self, branch_name):
        self.branch_name = branch_name
    
    def display_info(self):
        print(f"Bank: {Bank.bank_name}, Branch: {self.branch_name}")
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to: {cls.bank_name}")


if __name__ == "__main__":
    branch1 = Bank("Downtown")
    branch2 = Bank("Westside")
    
    branch1.display_info()
    branch2.display_info()
    
    Bank.change_bank_name("Global Banking Corporation")
    
    branch1.display_info()
    branch2.display_info()

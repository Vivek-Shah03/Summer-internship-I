class employee:
    emp_id = 101
    emp_name = "Unknown"
    salary = 10000
    def increament(self):
        bonus = self.salary * 0.1
        self.salary = self.salary + bonus
        print(f"Congratulations, {self.emp_id} {self.emp_name} your new salary is {self.salary}.")

e1 = employee()
e1.increament()

from Person import Person

# Inheritance in action
class Employee(Person):
    """A Person with a job"""
    def __init__(self, name, job_title):
        super().__init__(name)
        self.jobTitle = job_title

    def __repr__(self):
        return self.name + ": " + self.jobTitle

    def doWork(self):
        print(f'{self.name} is working as {self.jobTitle}')
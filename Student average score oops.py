class Student:
    def __init__(self, name, marks) :
        self.name = name
        self.marks = marks
        
    def avg_score(self):
        sum = 0
        for number in self.marks:
            sum += number
        print("Hello ",self.name ,"Your average score is:", sum/3)


s1 = Student("Kashif" , [99, 98, 97])
#create a method to find the marks average
s1.avg_score()
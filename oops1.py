from os import makedirs


class student():

  def __init__(self, name, marks):
    self.name = name 
    self.marks = marks

  def get_avg(self):
    sum = 0
    for value in self.marks:
        sum += value
    print("hi",self.name,"your avg score: ", sum/3)

s1 = student("tony kakkar",[98,99,98])
s1.get_avg()
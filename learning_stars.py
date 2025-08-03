class student():
    college_name = "ABC University"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student...")
        
s1 = student("John", 85)
print(s1.name, s1.marks)

s2 = student("Jane", 90)
print(s2.name, s2.marks)

print( s2.college_name)
    
 












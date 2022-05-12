class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
    def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
    def display(self, ob):
        print("Name: ", ob.name)
        print("Roll No: ", ob.rollno)
        print("Marks1: ", ob.m1)
        print("Marks2: ", ob.m2, end="\n")
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll

ls = []
obj = Student('',0,0,0)
print("\nOperations Used, ")
print("\n1.Accept Student Details")
print("\n2.Display Student Details")
print("\n3.Search Details of a Student")
print("\n4.Delete Details of a Student")
print("\n5.Update Student Details")
while(1):
    ch = int(input("Enter Your Choice: "))
    if(ch==1):
        obj.accept("A", 1, 100, 100)
        obj.accept("B", 2, 90, 90)
        obj.accept("C", 3, 80, 80)
    elif(ch==2):
        print("\n")
        print("\nList of Students")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            
    elif(ch==3):
        print("\nStudents Found")
        s = obj.search(2)
        obj.display(ls[s])


    elif(ch==4):
        obj.delete(2)
        print(ls.__len__())
        print("List After Deletion")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            

    elif(ch==5):
        obj.delete(3,2)
        print(ls.__len__())
        print("List After Updation")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            
    else:
        print("\n Thank You!")
    
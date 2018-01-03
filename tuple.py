from collections import namedtuple

Student = namedtuple('Student',['Name','Age','Sex','Email'])
s = Student('Jim',16,'Male','jim8721@gmail.com')

print s.Name
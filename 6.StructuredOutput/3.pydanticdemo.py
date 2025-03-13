from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str ='kunal'
    age: Optional[int]=None
    email:EmailStr
    cgpa: float=Field(gt=0, lt=10)

new_student={'age':'11','email':'gdfgdf@gmail.com', 'cgpa':1}
student=Student(**new_student)
dict_student=dict(student)
json_student=student.model_dump_json()
print(json_student)

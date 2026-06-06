student_dic = {
    "studnt": ["youssef","ali","ahmed"],
    "score": [90,60,70]
}

import pandas

students_DataFrame = pandas.DataFrame(student_dic)
print(students_DataFrame)

for(index,row) in students_DataFrame.iterrows():
    if row.score > 60:
        print(row)
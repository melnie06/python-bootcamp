# number = [1, 2, 3, 'hello']
# number = [1, 2, 3]
# number = list[int] = [1, 2, 3]


##HINTING - Tuple

# student_record = ('Jeff', 10, 'Prudent')

# student_record: tuple[str, int,str] = ('Jeff', 10, 'Prudent')

# student_record =  tuple[str, int,str]
# student_record: list [student_record] = [
#     'Jeff', 10, 'Prudent',
#     'May', 20, 'Prudent',
# ]

# # print(student_record)


# #HINTING DICTIONARY
# Task = dict[str, int]
# tasks: list[Task] = [
#     {'test': 3, 'code': 3}
    
# ]


from typing import Literal

Moves = Literal['Rock', 'Paper', 'Scissor']

def winner (move:Moves):
    return 1
                
print(Moves, Rock)
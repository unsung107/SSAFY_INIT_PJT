import csv

avengers = [
    {
        "name": "tony stark",
        "gender": "male",
        "appearances": 3068,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "male",
        "appearances": 2089,
        "years since joining": 52
    },
    {
        "name": "robert bruce banner",
        "gender": "female",
        "appearances": 1231235,
        "years since joining": 52123123
    }

]

with open('avengers.csv', 'w+', newline = '', encoding = 'utf-8') as f:
    #저장할 field의 이름을 미리 지정한다.
    fieldnames = ('name', 'gender')
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    #field 이름을 csv 최상단에 작성한다.
    writer.writeheader()
    
    # Dictionary 를 순회하며 key값에 맞는 value를 한줄씩 작성한다.
    for avenger in avengers:
        writer.writerow(avenger)

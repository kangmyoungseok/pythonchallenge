# http://www.pythonchallenge.com/pc/return/uzi.html

from datetime import date

date.today().today().isoweekday()
date(2022,2,20).isoweekday()

# 달력에 2/29일이 있다. -> 윤년.
# 1xx6인 윤년을 계산하면 다음과 같다

leap_year = [x for x in range(1016,2020,20)]
print(leap_year)

# leap year중, 2월 29일이 일요일인 날을 찾는다
answer = [year for year in leap_year if(date(year,2,29).isoweekday() == 7)]
print(answer)

# youngest : 1976
# second : 1776

# 1776-01-27일 출생 : mozart

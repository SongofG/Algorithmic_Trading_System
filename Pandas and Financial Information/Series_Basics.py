# Practicing and studying the basics of the pandas library!

from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)  # Similar to Python list type.

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao2)  # Similar to Python's dictionary type.

# Print indice and their values.
for date in kakao2.index:  # kakao2.index
    print(date)

for ending_price in kakao2.values:  # kakao2.values
    print(ending_price)

# Series Addition
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
print(merge)  # Note that the addition is done by the index.



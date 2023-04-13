per_cent_1 = {'name': 'ТКБ', 'stavka': 5.6}
per_cent_2 = {'name': 'СКБ', 'stavka': 5.9}
per_cent_3 = {'name': 'ВТБ', 'stavka': 4.28}
per_cent_4 = {'name': 'СБЕР', 'stavka': 4.0}

money = float(input("Введите сумму вашего капитала: ")) or int(input("Введите сумму вашего капитала: "))
deposit_1 = round(money*per_cent_1['stavka']/100,2)
deposit_2 = round(money*per_cent_2['stavka']/100,2)
deposit_3 = round(money*per_cent_3['stavka']/100,2)
deposit_4 = round(money*per_cent_4['stavka']/100,2)
D = [deposit_1, deposit_2, deposit_3, deposit_4]
print('deposit = ', list(map(round,D)))
D_max = round(max(D))
print('Максимальная сумма, которую вы можете заработать - ', D_max)

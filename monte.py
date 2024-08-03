import random
import copy


### 初期値 ###
SET = 20               # 何セット行うか
ODDS = 2               # オッズ何倍か
BET = 1000             # 1ユニットあたりのベット金額
UNIT_ARRAY = [1, 2, 3] # ユニット

### ユニット途中経過 ###
tmp_unit_array = [] 

### 結果 ###
payment = 0    # 支払い
game_count = 0 # ゲーム数
max_unit = 0   # 最大ユニット数
max_bet = 0    # 最大賭け金



### モンテカルロ法 検証 ###

# 指定したセット数完了するまで繰り返し
for i in range(SET):
  # セット数
  set_count = str(i+1)
  print('--------------------------------------')
  print('              ' + str(set_count) + 'セット目')
  print('--------------------------------------')
  set_payment = 0
  
  # ユニット配列セット
  tmp_unit_array = copy.copy(UNIT_ARRAY)

  # 1セット完了するまで繰り返し
  while True:
    # ゲーム数
    game_count += 1
    print('▽ ' + str(game_count) + 'ゲーム目' )


    # ユニット数計算
    unit = tmp_unit_array[0] + tmp_unit_array[-1]
    if unit > max_unit: max_unit = unit
    tmp_unit_list = ''
    for tmp_unit in tmp_unit_array:
      tmp_unit_list += str(tmp_unit) + ' '

    print(' ユニット  ：' + tmp_unit_list + '⇒ '+ str(unit))


    # 賭け金計算
    bet = BET * unit
    if bet > max_bet: max_bet = bet
    payment -= bet
    set_payment -= bet
    print(' 賭け金    ：' + str(bet))

    
    # ギャンブル！
    result = random.randrange(ODDS)
    if result == 1:
      # 勝ち
      payment += bet * ODDS
      set_payment += bet * ODDS
      win = (bet * ODDS) - bet
      print(' ゲーム結果：+' + str(win) + '円   ○ Win!')

      # ユニット配列から両端を削除
      tmp_unit_array = tmp_unit_array[1:-1]
    else:
      # 負け
      print(' ゲーム結果：-' + str(bet) + '円   × Lose')

      # ユニット配列の最後に今回のユニット数を追加
      tmp_unit_array.append(unit)
    
    print('\n')

    # ユニット配列が0か1つになったら1セット完了
    if len(tmp_unit_array) == 0 or len(tmp_unit_array) == 1:
      plus = ''
      if set_payment > 0: plus = '+'
      print(' ' + str(set_count) + 'セット目 収支：' + plus + str(set_payment) + '円')
      print('\n\n')
      break



### 結果 ###
plus = ''
if payment > 0: plus = '+'
print('######################################')
print('                 結果                  ')
print('######################################')
print('  セット数        ：' + str(SET))
print('  ゲーム数        ：' + str(game_count))
print('  オッズ          ：' + str(ODDS) + '倍')
print('  賭け金/1ユニット：' + str(BET) + '円')
print('  最大ユニット数  ：' + str(max_unit))
print('  最大賭け金      ：' + str(max_bet) + '円')
print('\n')
print('  合計収支        ：' + plus + str(payment) + '円')

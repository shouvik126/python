income=[10,30,35]
name=['ds','sdsds','sdsds','fsdfsd']
def double_monkey(dollar,name):
    #print('shouvik')
    return str(dollar*2)+name
new_income=list(map(double_monkey,income,name))
print(new_income)
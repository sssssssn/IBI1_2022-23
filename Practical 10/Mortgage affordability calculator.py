def function1(value,salary):
    a = 5*salary
#Get the value of five times salary
    if value <= a:
# compare whether house worth no more than five times of annual salary
        print('Yes')
    else:
        print('No')
#output the result
    return (value,salary)
    
value=input('value:')
salary=input('salary:')
(value,salary)=function1(value,salary)


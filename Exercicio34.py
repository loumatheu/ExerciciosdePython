#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
salary = float(input('Insira o salário do funcionário: '))

if salary > 1250:
    newsalary = salary * 1.10
    print(f'O novo salário do funcionário será: R${newsalary:.2f}')
else:
    newsalary = salary * 1.15
    print(f'O novo salário do funcionário será: R${newsalary:.2f}')

print('Aproveite o novo salário!')

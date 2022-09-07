#salary with bonus
#cara 1
nama = input()
fixed_salary = float(input())
total_sales = float(input())
seller_total_salary = fixed_salary + (15/100 * total_sales)
print("TOTAL =",round(seller_total_salary,2))


#cara 2
nama = input()
print("TOTAL =",round(float(input()) + ((15/100) * float(input())),2))

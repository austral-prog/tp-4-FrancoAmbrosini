def leap_year():
    year= int(input("ingrese un año: "))
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        print(f"El año {year} es bisiesto")
    else: 
        print(f"El año {year} no es bisiesto")
      

leap_year()

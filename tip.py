def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    #dollars_to_float(dollars)
    #percent_to_float(percent)



def dollars_to_float(d):
    # TODO
    m= float(d.strip('$'))
    return m



def percent_to_float(p):
    # TODO
    p= p.strip('%')
    j = float(p)/100
    return j


main()

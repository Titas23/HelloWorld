
def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer, 1)
    print("sheet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    print("")
    return rounded


calculate(16)
calculate(65)
calculate(88)
calculate(43)
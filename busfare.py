stopat = int(input("What number stop are you at?: "))
stopgo = int(input("What is the stop you want to go to?: "))
print(f"The fare from Stop {stopat} to Stop {stopgo} is ${(stopgo - stopat) * 2.50}")
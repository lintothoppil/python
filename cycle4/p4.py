print("Name: Linto Mathew Joy")
print("Rollno:41")
print("Experiment:14")


class Time:
    def __init__(self,hour=0,minute=0,sec=0):
        self.__hour=hour
        self.__min=minute
        self.__sec=sec

    def __add__(self,other):
        sec=(self.__sec+other.__sec)%60
        minute=(self.__min+other.__min+(self.__sec+other.__sec)//60)%60
        hour=(self.__hour+other.__hour+(self.__min+other.__min)//60)%24
        return Time(hour, minute, sec)

    def __str__(self):
        return f"Time: {self.__hour:02}hrs : {self.__min:02} min: {self.__sec:02} sec"


def create_time_from_input(prompt):
    while True:
        try:
            time_input = input(prompt)
            hour, minute, sec = map(int, time_input.split(":"))
            if not (0 <= hour < 24 and 0 <= minute < 60 and 0 <= sec < 60):
                print("Invalid time range")
                continue
            return Time(hour, minute, sec)
        except ValueError:
            print(f"Please enter the time in the format hh:mm:ss.")
t1 = create_time_from_input("Enter the first time (hh:mm:ss): ")
t2 = create_time_from_input("Enter the second time (hh:mm:ss): ")

t3 = t1 + t2
print(t3)
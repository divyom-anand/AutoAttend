import pandas as pd 
class attendance:

    def mark_attendance(self,a):
        self.df = pd.read_csv("source code/Attendance.csv")
        self.df.loc[self.df["student"]==a, "attendance"] +=1
        del self.df[self.df.columns[0]]
        self.df.to_csv("source code/Attendance.csv")

    def __init__(self) -> None:
        try:
            self.df= pd.read_csv("source code/Attendance.csv")
        except:
            d={'student': ["divyom", "aryan p"], 'attendance': [0, 0]}
            self.df=pd.DataFrame(data=d)
            self.df.to_csv("source code/Attendance.csv")
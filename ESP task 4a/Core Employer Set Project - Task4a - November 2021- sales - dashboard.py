import datetime
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt

df = pd.read_csv('Task_4a_data.csv', index_col='ID')

#main menu
def menu():
    print("\t\t****MAIN MENU****")
    print('1) Enter sales records')
    print('2) Run reports')
    x = int(input(""))
    return x

#reports menu
def menu2():
    print("**** Reports Dashboard ****")
    print("1. Individual Employee Report")
    print("2. Highest Sale Employee")
    x = int(input(""))
    return x



def ind_emp_check(df_r, id, date1, date2):
    df_r = df_r.loc[df.index == id]

    df_r = df_r.T[3:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    date1 = pd.to_datetime(date1, format='%d/%m/%Y')
    date2 = pd.to_datetime(date2, format='%d/%m/%Y')
    mask = (df_r['ID1'] >= date1) & (df_r['ID1'] <= date2)
    df_search = df_r.loc[mask]
    print(df_search)
    print('Total by id = {} is {}'.format(id, sum(df_search[id])))

    plt.bar(df_search['index'], df_search[id])
    plt.xticks(rotation=90)
    plt.show()

y = menu()
while y == 1 or y == 2:
    if y == 1:
        try:
            ID = int(input("Enter the Staff ID "))
            if ID not in df.index.values:
                print('yes')

            date1 = input("Enter Date in dd/mm/yy: ")
            day, month, year = date1.split("/")
            date1 = datetime.date(int(year), int(month), int(day))

            if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
                    dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
                print("Date is in the future")
            else:
                cost = float(input("Enter the cost : "))
                df.loc[ID, date1.strftime('%d/%m/%Y')] = cost
            # df.to_csv('test2.csv')
        except:
            print("\n\nError Occurred Please try again\n\n")
            y = menu()

    if y == 2:
        x = menu2()
        if x == 1:
            try:
                id = int(input("Enter the Employee Id : "))
                s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                day, month, year = s_date.split("/")
                s_date = datetime.date(int(year), int(month), int(day))

                e_date = input("Enter Date in dd/mm/yyyy: ")
                day, month, year = e_date.split("/")
                e_date = datetime.date(int(year), int(month), int(day))

                s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                ind_emp_check(df, id, s_date, e_date)
            except:
                print("\n\nError Occurred Please try again\n\n")
                x = menu2()
        temp = 0
        temp2 = ""
        myList = ["01/01/2021","02/01/2021","03/01/2021","04/01/2021","05/01/2021","06/01/2021","07/01/2021","08/01/2021","09/01/2021","10/01/2021","11/01/2021","12/01/2021","13/01/2021","14/01/2021","15/01/2021","16/01/2021","17/01/2021","18/01/2021","19/01/2021","20/01/2021","21/01/2021","22/01/2021","23/01/2021","24/01/2021","25/01/2021","26/01/2021","27/01/2021","28/01/2021","29/01/2021","30/01/2021","31/01/2021","01/02/2021","02/02/2021","03/02/2021","04/02/2021","05/02/2021","06/02/2021","07/02/2021","08/02/2021","09/02/2021","10/02/2021","11/02/2021","12/02/2021","13/02/2021","14/02/2021","15/02/2021","16/02/2021","17/02/2021","18/02/2021","19/02/2021","20/02/2021","21/02/2021","22/02/2021","23/02/2021","24/02/2021","25/02/2021","26/02/2021","27/02/2021","28/02/2021","01/03/2021","02/03/2021","03/03/2021","04/03/2021","05/03/2021","06/03/2021","07/03/2021","08/03/2021","09/03/2021","10/03/2021","11/03/2021","12/03/2021","13/03/2021","14/03/2021","15/03/2021","16/03/2021","17/03/2021","18/03/2021","19/03/2021","20/03/2021","21/03/2021","22/03/2021","23/03/2021","24/03/2021"]

        if x == 2:
            df=pd.read_csv("Task_4a_data.csv")
            for i in myList:
                high = df[i].max()
                if high > temp:
                    temp = high
                    temp2 = i
                else:
                    high = high
            print("the highest price sale made was £",high,"on the date",temp2)
            

        else:
            x = menu2()
    else:
        x = menu()
    x = menu()

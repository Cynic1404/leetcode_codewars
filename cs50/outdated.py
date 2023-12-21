#solution without try/except

months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    to_check=date.split(", ")
    if len(to_check)==2 and len(to_check[0].split())==2:
        month, year=date.split(", ")
        month, day = month.split()
        if month not in months or int(day)>31:
            continue
        else:
            month=months.index(month)+1
            break
    else:
        to_check=date.split("/")
        if len(to_check)==3 and all([i.isdigit() for i in to_check]):
            month, day, year = date.split("/")
            if int(day) > 31 or int(month) > 12:
                continue
            break
        else:
            continue


print(f"{year}-{int(month):02}-{int(day):02}")

print("what's your zodiac sign ?")
print("Note : capitalize the first letter of your birth month")
month=input("enter your birth month: ")
day=int(input("enter your bith day (1-31): "))
if (month == "March" and day >= 21) or (month == "April" and day <= 19) : sign = "Aries"
elif (month == "April" and day >= 20) or (month == "May" and day <= 20) : sign = "Taurus"
elif (month == "May" and day >= 21) or (month == "June" and day <= 20) : sign = "Gemini"
elif (month == "June" and day >= 21) or (month == "July" and day <= 22) : sign = "Cancer"
elif (month == "July" and day >= 23) or (month == "August" and day <= 22) : sign = "Leo"
elif (month == "August" and day >= 23) or (month == "September" and day <= 22) : sign = "Virgo"
elif (month == "September" and day >= 23) or (month == "October" and day <= 22) : sign = "Libra"
elif (month == "October" and day >= 23) or (month == "November" and day <= 21) : sign = "Scorpio" 
elif (month == "November" and day >= 22) or (month == "December" and day <= 21) : sign = "Sagittarius"
elif (month == "December" and day >= 22) or (month == "January" and day <= 19) : sign = "Capicorn"
elif (month == "January" and day >= 20) or (month == "February" and day <= 18) : sign = "Aquarius"
elif (month == "February" and day >= 19) or (month == "March" and day <= 20) : sign = "Pisces"
else : print("incorrect, check your input")
print(f"your zodiac sign is : {sign}")
#Enter the Curruncy Code,  Such as INR, USD, ERU
country = input("Enter Country Name : ").strip().upper()
rent = float(input("Total Rent Amount : "))
food = float(input("Total Food Cost : "))
electricity_unit = float(input("Electricity unit used : "))
charge_per_unit = float(input("Charge per Electricity Per Unit : "))
people = int(input("Number of People : "))

#Calculate the total Electricity Cost
electricity_cost = electricity_unit * charge_per_unit

#Add, Food, Rent, and Electricity Cost
total_bill = rent + food + electricity_cost

#Country Currency Symbol & Comma Style 
if country == "INDIA":
    currency = "₹"

elif country in ("UNITED STATES", "US", "USD", "USA"):
    currency = "$"

else:
    print("Country Not Supported")
    raise SystemExit


#Check that the Number of People is valid Before Dividing
if people > 0:
    share = total_bill / people

    if country == "INDIA":
        formatted_share = F"{share:.2f}"
        whole, decimal = formatted_share.split(".")
        last_three = whole[-3:]
        remaining = whole[:-3]

        if remaining:
            remaining = ",".join(
                [remaining[max(i - 2, 0):i] for i in range(len(remaining), 0, -2)][::-1]
            )
            formatted_share = remaining + "," + last_three + "." + decimal

        else:
            formatted_share = last_three + "." + decimal

    else:
        formatted_share = f"{share:,.2f}"

    print(f"Each Person Pays : {currency} {formatted_share}")

else:
    print("Number of People Must be Greater than Zero.")


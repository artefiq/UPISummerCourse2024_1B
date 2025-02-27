# First Case Study : Miles Per Gallon
# • Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track of several tankfuls of gasoline
#   by recording miles driven and gallons used for each tankful. Develop a sentinel-controlled-repetition script that prompts the
#   user to input the miles driven and gallons used for each tankful.
# • The script should calculate and display the miles per gallon obtained for each tankful. After processing all input information, the
#   script should calculate and display the combined miles per gallon obtained for all tankfuls (that is, total miles driven divided by
#   total gallons used).

def main():
    total_miles = 0
    total_gallons = 0

    while True:
        gallons = float(input("Enter the gallons used (-1 to end): "))
        if gallons == -1:
            break
        miles = float(input("Enter the miles driven: "))

        mpg = miles / gallons
        print(f"The miles/gallon for this tank was {mpg:.6f}")

        total_miles += miles
        total_gallons += gallons

    if total_gallons != 0:
        overall_mpg = total_miles / total_gallons
        print(f"The overall average miles/gallon was {overall_mpg:.6f}")
    else:
        print("No data to calculate overall average miles/gallon.")

if __name__ == "__main__":
    main()

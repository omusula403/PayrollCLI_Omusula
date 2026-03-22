import sys
import csv
import os


def main():
    company_name = input("Enter Company Name:")
    company_kra_pin = input("Enter Company KRA Pin: ")
    payroll_month_year = input("Enter Payroll Month and Year(eg December 2025 ): ")
    next_prompt = input("Type 'next' to proceed: ")
    if next_prompt != 'next':
        print("Program Stopped!")
        exit()

    input_method = input("Select Payroll Input Method\n"
                         "\t1. Manual employee entry\n"
                         "\t2. Upload employee file\n"
                         "Type '1' or '2': ")

    #manual employee entry
    if input_method == "1":
        while True:
                employee_name = input("Enter Employee Name: ")
                kra_pin = input("Enter Employee KRA Pin: ")
                print("\nEARNINGS")
                try:
                    print("\nBasic Salary")
                    basic_salary = float(input("Basic salary: "))

                    print("Allowances")
            
                    allowances = {}

                    #predefined allowances
                    allowances["House"] = float(input("House Allowance: "))
                    allowances["Transport"] = float(input("Commuter / Transport Allowance: "))
                    allowances["Medical"] = float(input("Medical Allowance: "))
                    allowances["Overtime"] = float(input("Overtime Allowance: "))
                    allowances["Meal"] = float(input("Meal / Luncheon Allowance: "))
                    allowances["Hardship"] = float(input("Hardship Allowance: "))
                    allowances["Risk"] = float(input("Risk Allowance: "))
                    allowances["Leave"] = float(input("Leave Allowance: "))

                    #additional allowance option
                    additional = input("\nFor Additional Allowances\n"
                                        "Type 'add' to enter (Type/Amount)\n"
                                        "Otherwise type 'none': ")
                    if additional.lower() == 'add':
                        while additional.lower() == "add":
                            allowance_type = input("Enter allowance type: ")
                            allowance_amount = float(input("Enter allowance amount: "))
                            allowances[allowance_type] = allowance_amount
                            additional = input("Add another allowance? (add/none): ")
                    elif additional.lower() == "none":
                        print("No additional allowances added.")

                    else:
                        print("Invalid option!")

                    #display all allowances
                    print("\nAllowance Summary")
                    total_allowances = 0

                    for name, amount in allowances.items():
                        print(name, ":", amount)
                        total_allowances += amount
                    print("Total Allowances:", total_allowances)

                    #Variable earnings
                    print("\nVariable Earnings")

                    variable_earnings = {}
                    variable_earnings["commissions"] = float(input("Commissions:"))
                    variable_earnings["bonuses"] = float(input("Bonuses:"))
                    variable_earnings["leave_pay"] = float(input("Leave Pay:"))

                    print("\nVariable Earnings Summary")
                    total_variable_earnings = 0

                    for name, amount in variable_earnings.items():
                        print(name, ":", amount)
                        total_variable_earnings += amount
                    print("Total Variable Earnings:", total_variable_earnings)

                    next_step = input("Type 'next' to Calculate Gross Income: ")

                    if next_step.lower() == "next":

                        print("\nGROSS PAY SUMMARY")
                        print(f"Basic Salary: {basic_salary}")
                        print(f"Total Allowances: {total_allowances}")
                        print(f"Total Variable Earnings: {total_variable_earnings}")
                        gross_income = basic_salary + total_allowances + total_variable_earnings
                        print("\nGross Income:", gross_income)


                    print("DISPLAY: DEDUCTIONS")



            #resident_status = input("Select Resident Status\n"
                                    #"\t1.Resident \n"
                                    #"\t2. Non Resident \n"
                                    #"Type '1' or '2': ")
            #if resident_status == "1":
                #Resident, Personal Relief applies
                #personal_relief = 2400

                #Non resident, Personal Relief = 0
            #elif resident_status == "2":
                #personal_relief = 0
            #else:
                 #print("Invalid option!")

            #Disability Status
            #pwd_status = input("Person With Disability?\n"
                               #"\t1.Yes \n"
                               #"\t1.No \n"
                               #"Type '1' or '2'): ")
            #if pwd_status == "1":
                #pwd, First 150'000 is exempted from taxation
                #exempt_amount = 150000
                #Taxable amount is what is above 150'000
                #taxable_for_paye = max(0, taxable_income - exempt_amount)
                # not pwd, no exemption
            #elif pwd_status == "2":
                #taxable_for_paye = taxable_income
            #else:
                 #print("Invalid option!")

            #Employee type
            #employee_type = input("Enter Employee Type "
                                  #"\t1.Primary  \n"
                                  #"\t2.Secondary')\n"
                                  #"Type '1' or '2'): ")
            #if employee_type == "1":
                #Primary employee, Personal Relief applies
                #personal_relief = 2400
            #elif employee_type == "2":
                #Secondary employee, Personal Relief = 0
                #personal_relief = 0
            #else:
                 #print("Invalid option!")


            #housing_type = ("Type of Housing \n"
                            #"\t1.Benefit not Given \n"
                            #"\t2.Employer's Owned House \n"
                            #"\t3.Employer's Rented House \n"
                            #"\t4.Agricultural Farm\n"
                            #"\t5.House to non full time service director\n"
                            #"Select one option: ")

                #Compute deductions
                    to_deductions = input("Type 'proceed' to calculate deductions: ").strip().lower()

                    if to_deductions == 'proceed':


                        #Open the CSV file containing tax rates; 'utf-8-sig' handles excel signatures
                        with open(r'C:\Users\Admin\Downloads\deductions_rates.csv', mode='r', encoding='utf-8-sig') as f:

                            #Convert the CSV into a list of dictionaries (keys are column headers)
                            rows = list(csv.DictReader(f))

                            #Initialize a counter for all deductions that happen before income tax is calculated
                            pre_tax_total = 0

                        #Initialize a dictionary to store specific deduction amounts by name ({'NSSF': 1080})
                        results = {}

                        #Loop through every rule in csv file
                        for row in rows:
                            #For rows with category as 'pre_tax'
                            if row["category"] == "pre_tax":
                                name = row["name"]
                                rate = float(row["rate"])
                                high = float(row["limit_high"])
                                mini = float(row["min_amount"])
                            #For rows with type as 'capped_pct'
                                if row["type"] == "capped_pct":
                                    amt = min(gross_income, high) * rate
                            #Rest of the rows with 'flat percentage'
                                else:
                                    amt = max(gross_income * rate, mini)
                                #Store the name with its amount in 'results dictionary'
                                results[name] = amt
                                #Add each amount to the total running tally of pre-tax deductions
                                pre_tax_total += amt

                        #Determine Taxable Income
                        taxable_income = gross_income - pre_tax_total

                        #Initialize a counter for PAYE
                        total_tax = 0
                        #Tracks the end of the last tax bracket e.g. 24,000
                        previous_limit = 0
                        #Loop through rows to identify tax bands
                        for row in rows:
                            #Identify rows that define tax bands
                            if row["category"] == "tax_band":
                                #Check if taxable income actually reaches into this specific tax bracket
                                limit = float(row["limit_high"])
                                rate = float(row["rate"])
                            #Check if taxable income actually reaches into this specific tax bracket
                                if taxable_income > previous_limit:
                                    #Isolate the amount that is above the current tax band
                                    taxable_slice = min(taxable_income, limit) - previous_limit
                                    #Multiply the isolated amount by the band's rate and add it to the total tax
                                    total_tax += (taxable_slice * rate)
                                #Continue with the rest of the tax bands upwards
                                previous_limit = limit

                        #Standard amount for relief and subtract it from total tax
                        personal_relief = 2400  # Or pull from CSV category 'relief'
                        final_paye = max(0, total_tax - personal_relief)

                        # Calculate totals deductions and net pay
                        total_deductions = pre_tax_total + final_paye
                        net_pay = gross_income - total_deductions

                        print("\nDISPLAY: DEDUCTIONS SUMMARY")
                        print("-" * 30)  # Adds a separator line
                        print("Pre-tax Deductions:")


                        #Use results.get('key', 0) to pull the values from your dictionary

                        print(f"\tNSSF:           {results.get('nssf', 0):,.2f}")
                        print(f"\tSHIF:           {results.get('shif', 0):,.2f}")
                        print(f"\tHousing Levy:   {results.get('housing_levy', 0):,.2f}")
                        print("-" * 30)

                        print(f"Taxable Income:     {taxable_income:,.2f}")
                        print(f"Income Tax (PAYE):  {final_paye:,.2f}")

                        print("-" * 30)

                        print(f"Total Deductions:   {total_deductions:,.2f}")
                        print(f"NET PAY:            {net_pay:,.2f}")
                        print("-" * 30)

                        #Define a unique filename for this employee
                        filename = f"Payslip_{employee_name.replace(' ', '_')}_{payroll_month_year.replace(' ', '_')}.csv"

                        #Write the data to the CSV file
                        with open(filename, mode='w', newline='') as payslip_file:
                            writer = csv.writer(payslip_file)

                            writer.writerow(["Company Name", company_name])
                            writer.writerow(["Payroll Month/Year", payroll_month_year])
                            writer.writerow(["Employee Name", employee_name])
                            writer.writerow(["KRA PIN", kra_pin])
                            writer.writerow(["   ", "   "])
                            writer.writerow(["Description", "Amount (Ksh)"])
                            writer.writerow(["Basic Salary", basic_salary])
                            writer.writerow(["Gross Income", gross_income])
                            writer.writerow(["NSSF", results.get('nssf', 0)])
                            writer.writerow(["SHIF", results.get('shif', 0)])
                            writer.writerow(["Housing Levy", results.get('housing_levy', 0)])
                            writer.writerow(["Taxable Income", taxable_income])
                            writer.writerow(["PAYE (Tax)", final_paye])
                            writer.writerow(["   ", "   "])
                            writer.writerow(["TOTAL DEDUCTIONS", total_deductions])
                            writer.writerow(["NET PAY", net_pay])

                        #Display path file for payslip to user
                        file_path = os.path.abspath(filename)
                        print("\n" + "-" * 50)
                        print(f"Payslip for {employee_name} Successfully Generated!")
                        print(f"File Location: {file_path}")
                        print("-" * 50)

                        repeat = input("Add New Employee? \n"
                                        "\t1. Yes \n"
                                        "\t2. No \n"
                                        "Type '1' or '2': ")
                        if repeat == '2':
                            print(f"Closing payroll session for {company_nam}")
                            break
                        elif repeat == '1':
                            print("-" * 30)
                            print("Restarting for new employee")
                        else:
                            print ("Invalid Input")


                        # Returns the data to your main program
                        #return results, final_paye

                    else:
                            print("Operation cancelled.")

                except ValueError:
                    print("Invalid Input")


    #upload employee file
    if input_method == "2":
        print("Your File headers should be: employee_name, employee_kra_pin, basic_salary, total_allowances, total_variable_earnings, gross_income")
        file_path_input = input("Enter the full path to your employee CSV file: ").strip().replace('"', '')

    try:
        with open(file_path_input, mode='r', encoding='utf-8-sig') as emp_file:
            # Load all employees into a list of dictionaries
            employees = list(csv.DictReader(emp_file))
            print(f"\n[SYSTEM] Found {len(employees)} employees. Starting batch processing for March 2026...")

            for emp in employees:
                # 1. Pull data from the current row
                employee_name = emp['employee_name']
                employee_kra_pin = emp['employee_kra_pin']
                basic = float(emp.get('basic_salary', 0))
                allow = float(emp.get('total_allowances', 0))
                variable_earnings = float(emp.get('total_variable_earnings', 0))

                gross_income = basic + allow + variable_earnings

                # Compute deductions
                to_deductions = input("Type 'proceed' to calculate deductions: ").strip().lower()

                if to_deductions == 'proceed':

                    # Open the CSV file containing tax rates; 'utf-8-sig' handles excel signatures
                    with open(r'C:\Users\Admin\Downloads\deductions_rates.csv', mode='r', encoding='utf-8-sig') as f:

                        # Convert the CSV into a list of dictionaries (keys are column headers)
                        rows = list(csv.DictReader(f))

                        # Initialize a counter for all deductions that happen before income tax is calculated
                        pre_tax_total = 0

                    # Initialize a dictionary to store specific deduction amounts by name ({'NSSF': 1080})
                    results = {}

                    # Loop through every rule in csv file
                    for row in rows:
                        # For rows with category as 'pre_tax'
                        if row["category"] == "pre_tax":
                            name = row["name"]
                            rate = float(row["rate"])
                            high = float(row["limit_high"])
                            mini = float(row["min_amount"])
                            # For rows with type as 'capped_pct'
                            if row["type"] == "capped_pct":
                                amt = min(gross_income, high) * rate
                            # Rest of the rows with 'flat percentage'
                            else:
                                amt = max(gross_income * rate, mini)
                            # Store the name with its amount in 'results dictionary'
                            results[name] = amt
                            # Add each amount to the total running tally of pre-tax deductions
                            pre_tax_total += amt

                    # Determine Taxable Income
                    taxable_income = gross_income - pre_tax_total

                    # Initialize a counter for PAYE
                    total_tax = 0
                    # Tracks the end of the last tax bracket e.g. 24,000
                    previous_limit = 0
                    # Loop through rows to identify tax bands
                    for row in rows:
                        # Identify rows that define tax bands
                        if row["category"] == "tax_band":
                            # Check if taxable income actually reaches into this specific tax bracket
                            limit = float(row["limit_high"])
                            rate = float(row["rate"])
                            # Check if taxable income actually reaches into this specific tax bracket
                            if taxable_income > previous_limit:
                                # Isolate the amount that is above the current tax band
                                taxable_slice = min(taxable_income, limit) - previous_limit
                                # Multiply the isolated amount by the band's rate and add it to the total tax
                                total_tax += (taxable_slice * rate)
                            # Continue with the rest of the tax bands upwards
                            previous_limit = limit

                    # Standard amount for relief and subtract it from total tax
                    personal_relief = 2400  # Or pull from CSV category 'relief'
                    final_paye = max(0, total_tax - personal_relief)

                    # Calculate totals deductions and net pay
                    total_deductions = pre_tax_total + final_paye
                    net_pay = gross_income - total_deductions

                    print("\nDISPLAY: DEDUCTIONS SUMMARY")
                    print("-" * 30)  # Adds a separator line
                    print("Pre-tax Deductions:")

                    # Use results.get('key', 0) to pull the values from your dictionary

                    print(f"\tNSSF:           {results.get('nssf', 0):,.2f}")
                    print(f"\tSHIF:           {results.get('shif', 0):,.2f}")
                    print(f"\tHousing Levy:   {results.get('housing_levy', 0):,.2f}")
                    print("-" * 30)

                    print(f"Taxable Income:     {taxable_income:,.2f}")
                    print(f"Income Tax (PAYE):  {final_paye:,.2f}")

                    print("-" * 30)

                    print(f"Total Deductions:   {total_deductions:,.2f}")
                    print(f"NET PAY:            {net_pay:,.2f}")
                    print("-" * 30)


                #Payslip generation
                safe_name = employee_name.replace(' ', '_')
                filename = f"Payslip_{safe_name}.csv"

                with open(filename, mode='w', newline='') as p_file:
                    writer = csv.writer(p_file)
                    writer.writerow(["PAYROLL RECORD", "MARCH 2026"])
                    writer.writerow(["Employee Name", employee_name])
                    writer.writerow(["KRA PIN", employee_kra_pin])
                    writer.writerow(["---", "---"])
                    writer.writerow(["Gross Income", f"{gross_income:,.2f}"])
                    writer.writerow(["NSSF", f"{results.get('nssf', 0):,.2f}"])
                    writer.writerow(["SHIF", f"{results.get('shif', 0):,.2f}"])
                    writer.writerow(["Housing Levy", f"{results.get('housing_levy', 0):,.2f}"])
                    writer.writerow(["PAYE (Tax)", f"{final_paye:,.2f}"])
                    writer.writerow(["---", "---"])
                    writer.writerow(["NET PAY", f"{net_pay:,.2f}"])

                # 3. Display the clickable path
                abs_path = os.path.abspath(filename)
                uri_path = f"file:///{abs_path.replace('\\', '/')}"
                print(f"Generated for {employee_name}: {uri_path}")

        print("\n" + "-" * 45)
        print("BATCH COMPLETED SUCCESSFULLY!")
        print("-" * 45)

    except FileNotFoundError:
        print("Error: The master employee file was not found.")
    except KeyError as e:
        print(f"Error: Your CSV is missing a required column header: {e}")
    #prints an error if input not 1 or 2
    else:
        print("Invalid Input")

    return 0


if __name__ == '__main__':
    sys.exit(main())
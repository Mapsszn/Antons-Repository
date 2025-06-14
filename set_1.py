def savings(gross_pay, tax_rate, expenses):
    x = gross_pay*tax_rate
    final_value = int(gross_pay - x - expenses)
    return final_value
def material_waste(total_material, material_units, num_jobs, job_consumption):
    x = num_jobs*job_consumption
    y = str(total_material - x) + str(material_units)
    return y
def interest(principal, rate, periods):
    x = rate*periods
    final_value = int(principal + (principal*x))
    return final_value
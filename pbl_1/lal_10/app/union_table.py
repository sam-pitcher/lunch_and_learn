import csv

file = 'app/table.csv'

def write_view_file(file=file):
    csv_rows = []
    sql_row = ""
    array_of_sql = []
    dimension_array = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        # print(field)

    for j in range(len(csv_rows) - 1):
        for i in range(len(csv_rows[1])-1):
            sql_row = sql_row + csv_rows[j][str(field[i])] + "' AS '" + field[i] + "', '" 
        sql_row = sql_row + csv_rows[j][str(field[len(csv_rows[0])-1])] + "' AS '" + field[len(csv_rows[0])-1] + "'"
        sql_row = "SELECT '" + sql_row
        sql_row = "(" + sql_row[:] + ") UNION ALL"

        # print(sql_row)
        array_of_sql.append(sql_row)
        sql_row = ""

    for i in range(len(csv_rows[1])-1):
        sql_row = sql_row + csv_rows[j + 1][str(field[i])] + "' AS '" + field[i] + "', '"
    sql_row = sql_row + csv_rows[j + 1][str(field[len(csv_rows[0])-1])] + "' AS '" + field[len(csv_rows[0])-1] + "'"
    sql_row = "SELECT '" + sql_row
    sql_row = "(" + sql_row[:] + ")"

    # print(sql_row)
    array_of_sql.append(sql_row)


    view_file_array = []
    view_file_array.append("view: my_view {")
    view_file_array.append("    derived_table: {")
    view_file_array.append("        sql:")
    for i in array_of_sql:
        view_file_array.append(i)
    view_file_array.append(";; }")
    view_file_array.append("")

    # add the dimensions

    for i in field:
        view_file_array.append("   dimension {}".format(i)+" {")
        view_file_array.append("       type: string")
        view_file_array.append("       sql: ${TABLE}."+"{}".format(i)+" ;;")
        view_file_array.append("    }")
        view_file_array.append("")

    view_file_array.append("}")

    return(view_file_array)

# write_view_file()




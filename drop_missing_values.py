import pandas as pd

def load_csv_cafe_sales():
    
    cafe_sales_data = pd.read_csv("Cafe_sales.csv")

    return cafe_sales_data


def drop_missing_values_on_acceptance_criteria(dataframe = None, acceptance_criteria_percentage=5, col = 'Transaction Date'):
    #if no dataframe provided, load dataframe from csv
    if(dataframe == None or dataframe is None):
        dataframe = load_csv_cafe_sales()

    #count the total missing rows
    count_missing_rows = dataframe[col].isnull().sum()

    total_rows = dataframe.shape[0]

    percent_of_missing_rows = count_missing_rows / total_rows * 100

    #if the percent of missing rows is greater than acceptance criteria, return value error
    if(percent_of_missing_rows > acceptance_criteria_percentage):
        raise ValueError("Percent of missing columns greater than acceptance criteria percent!")
    
    #remove null values in column
    dataframe = dataframe.dropna(subset=[col])

    print("Total rows: ", total_rows)
    print("Missing data row total: ", count_missing_rows)

    print("Percentage of missing rows: ", percent_of_missing_rows)

    #return cleaned dataframe
    return dataframe
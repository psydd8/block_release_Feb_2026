import pandas as pd
def product_price(dataframe):
    """
    Creates a df containing prices by item
    
    :param file_location: location of the csv file named Cafe_sales

    Created by Domingo Doria

    """

    df = dataframe
    summary = df.groupby(["Item"])["Price Per Unit"].agg(Price = "mean",Std="std").reset_index().sort_values("Item")
    if summary["Std"].sum() == 0:
        summary.drop(columns="Std", inplace=True)   
        return summary
    else:
        "Potenially, you have various prices per product"
    


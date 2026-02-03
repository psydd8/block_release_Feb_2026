import pandas as pd

file_path = r"C:\Users\ddoria002\OneDrive - PwC\MI\Data Science Apprenticeship\block_release_Feb_2026\Cafe_sales.csv"

ppu_by_item = pd.read_csv(file_path)

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


def multiply_price_by_quantity(file, prices):
    merged_datasets = pd.merge(left=file, right=prices, on="Item")
    merged_datasets["Total Spent"] = merged_datasets["Total Spent"].fillna(
    merged_datasets["Quantity"] * merged_datasets["Price"]
)

    return merged_datasets

print(multiply_price_by_quantity(ppu_by_item, product_price(ppu_by_item)))

    
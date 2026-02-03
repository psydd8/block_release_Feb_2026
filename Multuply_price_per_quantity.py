def multiply_price_by_quantity(file, prices):
    """
    Takes in the original csv Cafe_sales.csv and multiplies the quantities by the price per item.
    
    :param file: Cafe_sales.csv transformed into df
    :param prices: uses the product prices function.
    """
    merged_datasets = pd.merge(left=file, right=prices, on="Item")
    merged_datasets["Total Spent"] = merged_datasets["Total Spent"].fillna(
    merged_datasets["Quantity"] * merged_datasets["Price"]
)

    return merged_datasets

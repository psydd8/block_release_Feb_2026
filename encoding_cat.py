import pandas as pd

def enc_cat(dataf):
    """ 
    Encodes all categoric columns in Cafe_sales csv
    
    Arg:
        dataf : the cafe_sales dataset as a dataframe

    Returns:
        new dataframe with categoric columns encoded
    """
    location_map = {"Takeaway": 1, "In-store": 2}
    payment_map = {"Credit Card": 1, "Cash": 2, "Digital Wallet":3}
    item_map = {"Coffee": 1, "Cake": 2, "Cookie": 3, "Salad": 4, "Smoothie": 5, "Sandwich": 6, "Juice": 7, "Tea": 8}
    new_df = dataf.copy()
    new_df["Location"] = new_df["Location"].map(location_map)
    new_df["Payment Method"] =  new_df["Payment Method"].map(payment_map)
    new_df["Item"] = new_df["Item"].map(item_map)

    return new_df

#test enc_cat
# data_raw = pd.read_csv("block_release_Feb_2026\Cafe_sales.csv")
# print(data_raw["Item"].unique())
# print(data_raw["Payment Method"].unique())
# print(data_raw["Location"].unique())
# test = enc_cat(data_raw)
# print(test["Item"].unique())
# print(test["Payment Method"].unique())
# print(test["Location"].unique())


import pandas as pd


# Function to replace null values in the 'Price Per Unit' column using the value in the 'Item' column
def ppu_by_item(df = None, csv = None):
    # Allows for input of csv value, otherwise uses given dataframe
    if csv != None:
        cafe_sales = pd.read_csv('Cafe_sales.csv')
    elif df != None:
        cafe_sales = df
    else:
        return ValueError

    # Populates NA values in 'Price Per Unit' with their value in the 'Item' column
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].fillna(cafe_sales['Item'])
    
    # Replaces the new item values in the 'Price Per Unit' column with their constant prices
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Cake", 3)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Juice", 3)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Salad", 5)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Smoothie", 4)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Sandwich", 4)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Coffee", 2)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Tea", 1.5)
    cafe_sales['Price Per Unit'] = cafe_sales['Price Per Unit'].replace("Cookie", 1)

    return cafe_sales









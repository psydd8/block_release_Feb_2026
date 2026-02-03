# Add any other necessary functions as imports from their script

import pandas as pd

from linear_interpolation_ppu import *
from encoding_cat import *
from product_prices import *
from drop_missing_values import *
from item_price_by_quantity import *
from Multuply_price_per_quantity import *
from Data_Cleaning_Ed import *
from Item Graphing Tool import *

one = no_duplicates('Cafe_sales.csv')
two = replace_outliers_with_nan(one)
three = ppu_by_item(df = two)
four = product_price(three)
five = multiply_price_by_quantity(four)
six = drop_missing_values_on_acceptance_criteria(five)
seven = enc_cat()
eight = plot_item_sales_per_month()

eight.to_csv('cleaned_cafe_data.csv')

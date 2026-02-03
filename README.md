Set-up

Create environment

python -m venv venv

Activate

venv\Scripts\activate

Install

python -m pip install -r requirements.txt

Description of the dataset:

Our dataset contains data relating to transactions from a cafe.

Fields: Transaction ID	Item	Quantity	Price Per Unit	Total Spent	Payment Method	Location	Transaction Date

Rows: 10000 initially

Roles-Tasks:

Rayan:

Created a function to remove duplicate rows from the data.

Sam: Reverse engineering price per unit from the item name:

The function takes either a dataframe or csv as an input and returns as a dataframe.
Linear interpolation was used as a relationship was assumed between two columns.

A "main" python file was also created to let us run all the different functions within one file.

The reasonign was because the price per unit was a constant based on the value in the item column.

Domingo: Reverse engineering item from price per unit:

Outline of techniques:

Reasoning behind those techniques:

Dan, Rapha, Ed: Visualisations of the price per unit and cost:

Outline of techniques:

Reasoning behind those techniques:

Ollie: README & encoding payment method and location:

Added set up information to the read me. For encoding, encoded all categorical columns into numeric to increase performace, reduce storage requirements and enable further analysis/modelling.


Clive: Drop rows based on how many values are missing compared to total data e.g. 5% or below then drop

Created a function that calculates how many rows for a certain column are blank and then depending on a tolerance level will either drop or keep those rows.

Benyamin: README






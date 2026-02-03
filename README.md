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

Sam: Reverse engineering price per unit from the item:

Outline of techniques:

Reasoning behind those techniques:


Domingo: Reverse engineering item from price per unit:

Outline of techniques:

Reasoning behind those techniques:


Dan, Rapha, Ed: Visualisations of the price per unit and cost:

Outline of techniques:

Reasoning behind those techniques:

Ollie: README & encoding payment method and location:

Outline of techniques:

Reasoning behind those techniques:

Clive: Drop rows based on how many values are missing compared to total data e.g. 5% or below then drop

Outline of techniques:

Reasoning behind those techniques:

Benyamin: README










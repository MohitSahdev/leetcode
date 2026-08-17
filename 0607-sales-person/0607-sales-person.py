import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # RED company ka com_id
    red_company = company[company["name"] == "RED"]["com_id"]

    # RED ke saath order karne wale sales_id
    red_sales = orders[orders["com_id"].isin(red_company)]["sales_id"]

    # Jo salespersons RED ke saath order nahi karte
    result = sales_person[~sales_person["sales_id"].isin(red_sales)]

    return result[["name"]]
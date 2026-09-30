import pandas as pd

def sales_analysis(Sales: pd.DataFrame, Product: pd.DataFrame) -> pd.DataFrame:
    result = Sales.merge(
        Product,
        on='product_id',
        how='inner'
    )[['product_name', 'year', 'price']]

    return result

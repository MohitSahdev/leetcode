import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    count_orders = orders.groupby('customer_number').size().reset_index(name='order_count')
    
    result = count_orders[count_orders['order_count'] == count_orders['order_count'].max()]
    
    return result[['customer_number']]
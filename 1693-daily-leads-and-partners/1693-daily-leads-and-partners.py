import pandas as pd

def daily_leads_and_partners(DailySales: pd.DataFrame) -> pd.DataFrame:
    return (
        DailySales
        .groupby(['date_id', 'make_name'], as_index=False)
        .agg(
            unique_leads=('lead_id', 'nunique'),
            unique_partners=('partner_id', 'nunique')
        )
    )

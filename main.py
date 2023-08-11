import json
import pandas as pd

# path for data files
deals_path = "data/deals.json"
products_path = "data/products.json"

def read_json_data(file_path):
    """
    Function/method to convert json data into dataframe.

    Args:
        file_path (str): Name of file or path to file.
    Returns:
        dataframe: A dataframe object
    """

    df = pd.read_json(file_path)
    print("Created dataframe from '{}' with {} rows.".format(file_path,len(df)))

    return df

def create_commission_df(deals_df, products_df):
    """
    Function/method to create commission dataframe from deals dataframe and products dataframe.

    Args:
        deals_df (dataframe): Dataframe created from deals.json.
        products_df (dataframe): Dataframe created from products.json.

    """

    c_df = deals_df.merge(products_df, left_on='product_id', right_on='id', how='inner', suffixes=('','_drop'))
    commission_df = c_df[c_df.columns.drop(list(c_df.filter(regex='_drop')))]
    commission_df['commission'] = commission_df['quantity_products_sold'] * commission_df['product_amount'] * commission_df['commission_rate']
    
    return commission_df
    
def calculate_commission(sales_rep_name, start_date, end_date, commission_df):
    """
    Function/method to calculate commission for a sales rep in a given time period and print result.

    Args:
        sales_rep_name (str): Name of the sales rep to calculate commission for.
        start_date (str): Starting date for the date range where commissions will be valid.
        end_date (str): Ending date for the date range where commissions will be valid.

    """

    rep_df = commission_df[(commission_df['sales_rep_name'].str.contains(sales_rep_name)) & ((commission_df['date'] > start_date) & (commission_df['date'] <= end_date))]

    total_commission = rep_df['commission'].sum()
    print("{} earned ${:.2f} in commission between {} and {}.".format(sales_rep_name, total_commission, start_date, end_date))

def main():

    deals_df = read_json_data(deals_path)
    products_df = read_json_data(products_path)
    commission_df = create_commission_df(deals_df, products_df)
    
    calculate_commission(sales_rep_name="Ian", start_date="2023-01-01", end_date="2023-4-30", commission_df=commission_df)
    calculate_commission(sales_rep_name="David", start_date="2023-04-01", end_date="2023-06-30", commission_df=commission_df)
    calculate_commission(sales_rep_name="Poppy", start_date="2023-03-01", end_date="2023-5-30", commission_df=commission_df)
    
if __name__ == "__main__":
    main()
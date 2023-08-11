import unittest
import pandas as pd
import main

class TestMain(unittest.TestCase):

    def test_create_commission_df(self):
        deals = [
            {
                "id": 1,
                "sales_rep_name": "Alvin",
                "date": "2023-03-02",
                "quantity_products_sold": 2,
                "product_id": 7,
                "has_2x_multiplier": 0
            }
        ]
        deals_df = pd.DataFrame(deals)

        products = [
            {
                "id": 1,
                "name": "Product_1",
                "product_amount": 1000,
                "commission_rate": 0.05
            }
        ]
        products_df = pd.DataFrame(products)

        result = main.create_commission_df(deals_df, products_df)
        self.assertTrue(result.empty)
    
    def test_calculate_commission(self):
        commission = [
            {
                "id": 1,
                "sales_rep_name": "Alvin",
                "date": "2023-03-02",
                "quantity_products_sold": 1,
                "product_id": 1,
                "has_2x_multiplier": 0,
                "name": "Product_1",
                "product_amount": 1000,
                "commission_rate": 0.05,
                "commission": 50
            },
            {
                "id": 2,
                "sales_rep_name": "Alvin",
                "date": "2023-03-02",
                "quantity_products_sold": 2,
                "product_id": 1,
                "has_2x_multiplier": 0,
                "name": "Product_1",
                "product_amount": 1000,
                "commission_rate": 0.05,
                "commission": 100
            },
            {
                "id": 3,
                "sales_rep_name": "Alvin",
                "date": "2023-03-01",
                "quantity_products_sold": 3,
                "product_id": 1,
                "has_2x_multiplier": 0,
                "name": "Product_1",
                "product_amount": 1000,
                "commission_rate": 0.05,
                "commission": 150
            },
        ]
        commission_df = pd.DataFrame(commission)

        result = main.calculate_commission("Alvin", "2023-03-01", "2023-03-02", commission_df)
        self.assertEqual(result, 150)

if __name__ == '__main__':
    unittest.main()
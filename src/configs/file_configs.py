from src.configs.schemas import CUSTOMER_SCHEMA, SALES_SCHEMA

CUSTOMER_CONFIG = {
    "schema": CUSTOMER_SCHEMA,
    "location": "./data/customer/",
    "file_pattern": r'customer_\d{4}\d{2}\d{2}\.csv',
    "key_columns": ["customer_id"],
    "data_type": 'full',
    "file_type": "csv",
    "read_args": {
        "sep": ","
    }
}

SALES_CONFIG = {
    "schema": SALES_SCHEMA,
    "location": "./data/sales/",  # Corrected location 
    "file_pattern": r'sales_\d{4}\d{2}\d{2}\.txt',  #(from ".parquet" to ".txt")
    "key_columns": ["sale_id"],
    "data_type": 'transactional',
    "file_type": "csv",
    "read_args": {
        "sep": "~",  # Corrected separator (from "," to "~")
        "names": list(map(lambda x: x['name'], SALES_SCHEMA)),
    }
}

CONFIGS = {
    "customer": CUSTOMER_CONFIG,
    "sales": SALES_CONFIG,  # Uncommented sales config
    # "product": PRODUCT_CONFIG
}
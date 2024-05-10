from snowflake.snowpark.functions import col

def filter_by_country(session, table_name, country):
  df = session.table(table_name)
  return df.filter(col("country") == country)
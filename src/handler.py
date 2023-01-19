import pandas as pd


def get_response_from_table(category: str):
    categories_table = pd.read_excel('CTFriend_категории.xlsx', na_filter=True)
    resp_row = categories_table.loc[
        categories_table['Категория'] == category]
    resp = list(resp_row['Ответ'])[0]
    return resp

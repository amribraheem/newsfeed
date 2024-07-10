
def dict_from_row(row, cursor):
    if row is None:
        return None
    col_names = [desc[0] for desc in cursor.description]
    return dict(zip(col_names, row))
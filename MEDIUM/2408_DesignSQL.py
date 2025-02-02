"""
You are given two string arrays, names and columns, both of size n. 
The ith table is represented by the name names[i] and contains columns[i] number of columns.

You need to implement a class that supports the following operations:

Insert a row in a specific table with an id assigned using an auto-increment method, 
where the id of the first inserted row is 1, 
and the id of each new row inserted into the same table is one greater than the id of the last inserted row, 
even if the last row was removed.

Remove a row from a specific table. 
Removing a row does not affect the id of the next inserted row.

Select a specific cell from any table and return its value.

Export all rows from any table in csv format.

Implement the SQL class:

SQL(String[] names, int[] columns)
Creates the n tables.

bool ins(String name, String[] row)
Inserts row into the table name and returns true.
If row.length does not match the expected number of columns, or name is not a valid table, returns false without any insertion.

void rmv(String name, int rowId)
Removes the row rowId from the table name.
If name is not a valid table or there is no row with id rowId, no removal is performed.

String sel(String name, int rowId, int columnId)
Returns the value of the cell at the specified rowId and columnId in the table name.
If name is not a valid table, or the cell (rowId, columnId) is invalid, returns "<null>".

String[] exp(String name)
Returns the rows present in the table name.
If name is not a valid table, returns an empty array. Each row is represented as a string, 
with each cell value (including the row's id) separated by a ",".
"""

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.rowIds = {}
        self.cols_map = {}
        self.tables = {}
        for i in range(len(names)):
            self.rowIds[names[i]] = 1
            self.cols_map[names[i]] = columns[i]
        for i in self.cols_map.keys():
            self.tables[f"table_{i}"] = {}

    def ins(self, name: str, row: List[str]) -> bool:
        if(name in self.cols_map.keys() and len(row) == self.cols_map[name]):
            self.tables[f"table_{name}"][self.rowIds[name]] =  row 
            self.rowIds[name] += 1
            return True
        else:
            return False

    def rmv(self, name: str, rowId: int) -> None:
        if(f"table_{name}" in self.tables.keys()):
            if(rowId in self.tables[f"table_{name}"].keys()):
                del self.tables[f"table_{name}"][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if(f"table_{name}" in self.tables.keys()):
            if(rowId in self.tables[f"table_{name}"].keys()):
                for i in range(len(self.tables[f"table_{name}"][rowId])):
                    if(i+1 == columnId):
                        return self.tables[f"table_{name}"][rowId][i]
        return "<null>"

    def exp(self, name: str) -> List[str]:
        flat_list = []
        
        if(f"table_{name}" in self.tables.keys()):
            for i in self.tables[f"table_{name}"].keys():
                row = str(i) + ","
                for j in self.tables[f"table_{name}"][i]:
                    row += str(j) + ","
                flat_list.append(row.rstrip(','))
        return flat_list

"""

"""
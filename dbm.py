import os.path, sqlite3 as sql


class DatabaseModel:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.connection = sql.connect(os.path.abspath('lawyer_helper_db.sqlite3'))
            cls.__instance.cursor = cls.__instance.connection.cursor()
            cls.__instance.prop = _Prop()
            cls.__instance.services = _Services()
            cls.__instance.contracts = _Contracts()
            cls.__instance.acts = _Acts()
            cls.__instance.ce_orders = _CashExpenseOrders()
            cls.__instance.cr_orders = _CashReceiptOrders()
        return cls.__instance

    def __init__(self):
        try: self.init_tables()
        except: pass

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def init_tables(self):
        self.cursor.execute('''CREATE TABLE "contracts" ("number" TEXT, "service" TEXT, "company" TEXT, "contract_date" TEXT, "agent" TEXT, "phone" TEXT, "passport" TEXT, "birthday" TEXT, "price" TEXT, "first_price" TEXT, "second_price" TEXT, "contract_end_date" TEXT, "name" TEXT, "path" TEXT)''')
        self.cursor.execute('''CREATE TABLE "acts" ("number" TEXT, "service" TEXT, "date" TEXT, "agent" TEXT, "company" TEXT, "price" TEXT, "path" TEXT)''')
        self.cursor.execute('''CREATE TABLE "ce_orders" ("number" TEXT, "service" TEXT, "date" TEXT, "agent" TEXT, "price" TEXT, "addiction" TEXT, "document" TEXT, "document_code" TEXT, "document_issue_date" TEXT, "document_issue_place" TEXT, "path" TEXT)''')
        self.cursor.execute('''CREATE TABLE "cr_orders" ("number" TEXT, "type" TEXT, "service" TEXT, "date" TEXT, "agent" TEXT, "price" TEXT, "path" TEXT)''')
        self.cursor.execute('''CREATE TABLE "services" ("table" INTEGER)''')
        self.cursor.execute('''CREATE TABLE "props" ("ask_for_delete" INTEGER, "filter_with_hidden_columns" INTEGER, "show_contract_info" INTEGER, "number" INTEGER, "column_0" INTEGER, "column_1" INTEGER, "column_2" INTEGER, "column_3" INTEGER, "column_4" INTEGER, "column_5" INTEGER, "column_6" INTEGER, "column_7" INTEGER, "column_8" INTEGER, "column_9" INTEGER, "column_10" INTEGER, "column_11" INTEGER, "column_12" INTEGER, "column_13" INTEGER)''')
        self.connection.commit()


class _Prop:
    def __init__(self):
        dbm = DatabaseModel()
        self.connection = dbm.connection
        self.cursor = dbm.cursor

    def _get_props(self):
        self.cursor.execute(f'''SELECT * FROM "props"''')
        props = self.cursor.fetchall()
        if not props:
            self.cursor.execute(f'''INSERT INTO "props" VALUES ({("'1', " * 18)[:-2]})''')
            self.connection.commit()
            return self._get_props()
        return props[0]

    def get_ask_for_delete(self):
        return self._get_props()[0] == 1

    def toggle_ask_for_delete(self):
        self.cursor.execute(f'''UPDATE "props" SET "ask_for_delete" = "{1 - self.get_ask_for_delete()}" WHERE "ROWID" = 1''')
        self.connection.commit()

    def get_filter_with_hidden_columns(self):
        return self._get_props()[1] == 1

    def toggle_filter_with_hidden_columns(self):
        self.cursor.execute(f'''UPDATE "props" SET "filter_with_hidden_columns" = "{1 - self.get_filter_with_hidden_columns()}" WHERE "ROWID" = 1''')
        self.connection.commit()

    def get_show_contract_info(self):
        return self._get_props()[2] == 1

    def toggle_show_contract_info(self):
        self.cursor.execute(f'''UPDATE "props" SET "show_contract_info" = "{1 - self.get_show_contract_info()}" WHERE "ROWID" = 1''')
        self.connection.commit()

    def get_visible_columns(self):
        visible_columns = []
        for column, visible in enumerate(self._get_props()[4:]):
            if visible == 1: visible_columns.append(column)
        return visible_columns

    def get_column_visible(self, column):
        return self._get_props()[4 + column] == 1

    def toggle_column_visible(self, column):
        self.cursor.execute(f'''UPDATE "props" SET "column_{column}" = "{1 - self.get_column_visible(column)}" WHERE "ROWID" = 1''')
        self.connection.commit()


class _Services:
    def __init__(self):
        dbm = DatabaseModel()
        self.connection = dbm.connection
        self.cursor = dbm.cursor

    def get_all(self):
        self.cursor.execute(f'''SELECT * FROM "services"''')
        return [service[0] for service in self.cursor.fetchall()]

    def add(self, title):
        self.cursor.execute(f'''INSERT INTO "services" VALUES ('{title}')''')
        self.connection.commit()

    def delete(self, title):
        self.cursor.execute(f'''DELETE FROM "services" WHERE "table" = "{title}"''')
        self.connection.commit()


class _LHTable:
    def __init__(self):
        dbm = DatabaseModel()
        self.connection = dbm.connection
        self.cursor = dbm.cursor
        self.table = None

    def get(self, number):
        self.cursor.execute(f'''SELECT * FROM "{self.table}" WHERE "number" = "{number}"''')
        try: return self.cursor.fetchall()[0]
        except: return []

    def get_all(self):
        self.cursor.execute(f'''SELECT * FROM "{self.table}"''')
        return self.cursor.fetchall()

    def add(self, fields):
        self.cursor.execute(f'''INSERT INTO "{self.table}" VALUES ('{"', '".join(list(fields))}')''')
        self.connection.commit()

    def delete(self, number):
        self.cursor.execute(f'''DELETE FROM "{self.table}" WHERE "number" = "{number}"''')
        self.connection.commit()

    def update(self, fields):
        self.delete(fields[0])
        self.add(fields)

    def update_path(self, path, number):
        self.cursor.execute(f'''UPDATE "{self.table}" SET "path" = "{path}" WHERE "number" == "{number}"''')


class _Contracts(_LHTable):
    def __init__(self):
        super().__init__()
        self.table = "contracts"

    def add(self, fields):
        super().add(fields)
        self.increment_number()

    def get_number(self):
        return DatabaseModel().prop._get_props()[3]

    def increment_number(self):
        self.cursor.execute(f'''UPDATE "props" SET "number" = "{self.get_number() + 1}"''')
        self.connection.commit()

    def update_name(self, name, number):
        self.cursor.execute(f'''UPDATE "contracts" SET "name" = "{name}" WHERE "number" == "{number}"''')
        self.connection.commit()


class _Acts(_LHTable):
    def __init__(self):
        super().__init__()
        self.table = "acts"


class _CashExpenseOrders(_LHTable):
    def __init__(self):
        super().__init__()
        self.table = "ce_orders"


class _CashReceiptOrders(_LHTable):
    def __init__(self):
        super().__init__()
        self.table = "cr_orders"

    def get(self, number):
        self.cursor.execute(f'''SELECT * FROM "{self.table}" WHERE "number" = "{number}"''')
        return self.cursor.fetchall()

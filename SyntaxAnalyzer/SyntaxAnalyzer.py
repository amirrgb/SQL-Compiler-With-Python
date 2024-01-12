class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token : str = ""
        self.index = 0
        self.reserved_keywords = sql_reserved_keywords = [
            "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER",
            "JOIN", "INNER", "LEFT", "RIGHT", "FULL", "WHERE", "GROUP BY", "ORDER BY",
            "HAVING", "UNION", "ALL", "AND", "OR", "NOT", "NULL", "TRUE", "FALSE",
            "BETWEEN", "LIKE", "AS", "ON", "IS", "IN", "EXISTS", "CASE", "WHEN",
            "THEN", "ELSE", "END", "DISTINCT", "TOP", "LIMIT", "AUTO_INCREMENT", "SERIAL", "ROWNUM", "SYSDATE", "CURRENT_TIMESTAMP",
            "IDENTITY", "NOCHECK", "CASCADE", "FOR"]

 
    def consume(self):
        # if self.tokens[self.index]:
            self.current_token = str(self.tokens[self.index]).upper()
            print("current token: ", self.current_token , "index: ", self.index)
            self.index += 1
            

    def previous(self):
        try :
            return "After " + self.tokens[self.index - 2]   
        except IndexError:
            return None

    def match(self, expected_token):    
        if self.current_token.upper() == str(expected_token).upper():
            self.consume()
        else:
               raise SyntaxError(f"{self.previous()} Expected {expected_token} but found {self.current_token}")    

    def match_identifier(self):
        if self.current_token.isidentifier():
            if self.current_token not in self.reserved_keywords:
                self.consume()
            else:
                raise SyntaxError(f"{self.previous()} given {self.current_token} is a keyword")
        else:
            raise SyntaxError(f"{self.previous()} Expected identifier but found {self.current_token}")

    def constraint(self):
        if self.current_token == "PRIMARY":
            self.match("PRIMARY")
            self.match("KEY")
            self.match("(")
            self.match_identifier()
            while self.current_token == ",":
                self.consume()
                self.match_identifier()
            self.match(")")
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    print("here1")
                    self.column_list()
                else:
                    print("here2")
                    self.constraint_list()  

        elif self.current_token == "FOREIGN":
            self.match("FOREIGN")
            self.match("KEY")
            self.match("(")
            self.match_identifier()
            self.match(")")
            self.match("REFERENCES")
            self.match_identifier()
            self.match("(")
            self.match_identifier()
            self.match(")")
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    print("here1")
                    self.column_list()
                else:
                    print("here2")
                    self.constraint_list()  

        elif self.current_token in ["NOT", "UNIQUE"]:
            self.consume()
            if self.current_token == ",":
                self.consume()
                if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                    print("here1")
                    self.column_list()
                else:
                    print("here2")
                    self.constraint_list()   

        else:
            raise SyntaxError(f"{self.previous()} Unexpected token: {self.current_token}")

    def constraint_list(self):
        if self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]: # more constraints? 
            self.constraint()
            while self.current_token == ",":
                self.constraint()
                self.consume() 

    def check_numeric(self):
        try:
            float_token = float(self.current_token)
        except ValueError:
            raise SyntaxError(f"{self.previous()} {self.current_token} is not numeric")
        self.consume()

    def data_type(self):
        if self.current_token.upper() in ["INT", "VARCHAR", "DATE", "FLOAT", "DECIMAL"]:  # more data types? #test of date and float
            self.consume()
            if self.current_token == "(":
                self.match("(")
                self.check_numeric()
                self.match(")")
        else:
            raise SyntaxError(f"{self.previous()} Unexpected token: {self.current_token}")

    def column_constraint(self):
        if not self.current_token == ",":
            if self.current_token == "PRIMARY":
                self.match("PRIMARY")
                self.match("KEY")
            elif self.current_token == "FOREIGN":
                self.match("FOREIGN")
                self.match("KEY")
                self.match("REFERENCES")
                self.match_identifier()
                self.match("(")
                self.match_identifier()
                self.match(")")
            elif self.current_token == "NOT":
                self.match("NOT")
                self.match("NULL")
            elif self.current_token == "UNIQUE" :
                self.match("UNIQUE")
            elif self.current_token == "DEFAULT" :
                self.consume()
                self.check_numeric()
        
    def column_def(self):
        self.match_identifier()
        self.data_type()
        while not self.current_token == "," :
            self.column_constraint()

    def column_list(self):
        self.column_def()
        while self.current_token == ",":
            self.consume()
            if not self.current_token.upper() in ["PRIMARY", "FOREIGN", "NOT", "UNIQUE"]:
                self.column_def()
            else:
                break 

    def statement(self):
        self.match("CREATE")
        self.match("TABLE")
        self.match_identifier()
        self.match("(")
        self.column_list()
        self.constraint_list()
        self.match(")")
        print(" - -- -current token: ", self.current_token , "index: ", self.index)
        if self.current_token == ";":
            print("Accepted.")
        else:
            raise SyntaxError(f"{self.previous()} Not finishing with ; and finished with {self.current_token}" )    

    def parse(self):
        self.consume()
        self.statement()
    

    "create table users (id int, name varchar(50) defalut 'bye bye);"
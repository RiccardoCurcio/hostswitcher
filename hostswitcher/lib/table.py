
class table:
    def print_table(titles=list(), data=list()):

        def __print_separator_line():
            counter = 4
            for i in range(columns_counter):
                counter = counter + columns_width[i] + (columns_counter-2)*2
            print("-" * counter )

        try:
            columns_counter = len(titles)
            table_data = [titles]
            for row in data:
                table_data.append(row)
            
            columns_width = [0,0,0]
            # get max string
            for row in table_data:
                for i in range(columns_counter):
                    width = len(row[i])
                    if width > columns_width[i]:
                        columns_width[i] = width
    
            __print_separator_line()
            for row in table_data:
                string_row=str('| ')
                for i in range(columns_counter):
                    string_row = '%s%s | ' % (string_row, row[i].ljust(columns_width[i]))
                print(string_row)
                __print_separator_line()

        except Exception as e:
            self.log.error(e)
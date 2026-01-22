
class MessageReader():

    def get_table(self, conn):

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM messages")

        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        return colums , rows

    #user can do it itself ...
    #def create_file(self, colums, rows):
        
    #    data = {"colums": colums, "rows": rows}
        
    #    buffer = io.BytesIO(json.dumps(data).encode("utf-8"))
    #    buffer.seek(0)

    #    return buffer
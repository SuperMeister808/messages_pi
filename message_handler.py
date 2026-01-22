
from title import CollectTitle
from message import CollectMessage
from connections import CollectConnections
from database import Database

class MessageHandler():

        def extract_data(self, data):

                title = data["title"]
                message = data["message"]
        
                return title , message

        def collect_data(self, conn, title, message):


                t = CollectTitle(title)   
                m = CollectMessage(message)
                c = CollectConnections(conn)
        
                t.collect_title()
                m.collect_messages()
                c.collect_connection()

        def write_data(self, conn, title, message):
        
                d = Database(conn)
                d.add_message(title, message)

        def clear_data(self):

                CollectConnections.clear_connections()
                CollectMessage.clear_messages()
                CollectTitle.clear_titles()
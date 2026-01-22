
from server import Server
from message_handler import MessageHandler
from message_reader import MessageReader

def main():

    message_handler = MessageHandler()
    message_reader = MessageReader()

    s = Server("0.0.0.0", 5000, message_handler, message_reader)
    s.run_server()

if __name__ == "__main__":

    main()
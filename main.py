
from server import Server

if __name__ == "__main__":

    s = Server("0.0.0.0", 5000)
    s.run_server()

# POST_PI Server

This is a Flask server to send messages from your computer to a Raspberry Pi.  

Messages are stored in a local SQLite database (`messages.db`) and also collected in in-memory collection classes for testing.

---

## Endpoints

### POST /send

**Description:**  
Send data as JSON with `title` and `message`.

**Request Example:**
```json
{
  "title": "My title",
  "message": "Hello world!"
}

**Response Examples:**
{"Success": "Thanks for your request!"}  // 200 OK
{"Error": "Content Type application/json not found!"}  // 405
{"Error": "Bad Request"}  // 400
{"Error": "Keys not found"}  // 405

### GET /get

**Description:**
Returns all messages stored in messages.db

**Response Example:**
{
  "columns": ["title", "message"],
  "rows": [
    ["My title", "Hello world!"],
    ["Another title", "Another message"]
  ]
}

**Error Example:**
{"Error": "No table found!"}  // 405

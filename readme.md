### Take home assignment challenge: 
The take home consists of implementing a back_end API serving the data from items.csv, orders.xml and users.json  

The API should be implemented in Python using Flask, it should expose the following endpoints:  

- **GET /users:** Gets a list of users
- **GET /user/{id}:** Gets a user by ID
- **POST /user:** Validates the data and creates a user
- **GET /user/{id}/orders:** Gets the relevant orders for one user
- **GET /user/{id}/order_items:** Gets the items that have ever been order by a user   

# Tip: 
A good separation of concern between API layer and data-fetching layer allows for reusability and a more flexible codebase   

# Bonus: 
- Implement sorting and ordering on GET endpoints
- Unit testing

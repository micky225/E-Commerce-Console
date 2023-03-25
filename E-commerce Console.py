# Features
# 1. Register - DONE
# 2. Login - DONE
# 3. List products - DONE
# 4. Add to cart - DONE
# 5. Checkout - DONE
cart = []
user_db = []
item_db = [
    {"name":"iphone_12_pro      ",  "price":  6400},
    {"name":"Samsung_s22_ultra  ", "price": 7200},
    {"name":"Google_pixel_4     " , "price": 3500},
    {"name":"Apple_series_4     ", "price": 1500},
    {"name":"Samsung_fold_4     ", "price": 22000},
    {"name":"Airpods_pro_2      ", "price": 3100},
]


# Query functions
def create_user(fullname, username, password):
    for user in user_db:
        if username == user["username"]:
            return False 
    
    # Create the new user 
    new_user = {"fullname":fullname, "username": username, "password":password}
    # Add the new user to the db
    user_db.append(new_user)
    return new_user

def get_user(username):
    for user in user_db:
        if user["username"] == username:
            return user 
    return False

# Login command for users that couldn't login and  want register a new command
def login_user(username, password):
    for user in user_db:
        if user["username"] == username and user["password"] == password:
            return user 
    return False

def login_1_user(username, password):
    for user in user_db:
        if user["username"] == username and user["password"] == password:
            return user 
    return False



# Auth functions
def register():
    print("=====================================")
    print("Registration Page")
    print("=====================================")
    fullname = input("Fullname : ")
    username = input("Username : ")
    password = input("Password : ")
    
    # Create the user
    user = create_user(fullname, username, password)
    if user:
        login()
    else:
        print("Username not available")
        print("Try Again")
        register()


def login():
    print("=====================================")
    print("Login Page")
    print("=====================================")
    username = input("Username : ")
    password = input("Password : ")
    user = login_1_user(username, password)
    if user:
        main_page()
    else:
        print("Invalid username and password provided. Please try again")
        login()

# Login command for users that couldn't login and  want register a new command
def login_invalid_user():
    print("=====================================")
    print("Login Page")
    print("=====================================")
    username = input("Username : ")
    password = input("Password : ")
    user = login_user(username, password)
    if user:
        main_page()
    else:
        print("Invalid username or password provided!!. Please try again or press one to register a new account")
        auth()

# 
def auth():
    
    print("""
    1. Register 2. Login
    """)
    user_input = input("Response: ")
    if user_input == "1":
        register()
    elif user_input == "2":
        login_invalid_user()
    else:
        print("Wrong input")    
        
     
# Main page
def main_page():
    print("                          ")
    print   ("AVAILABLE  PRODUCTS")
    print("==========================")
    for index, item in enumerate(item_db):  
        print(index+1, item['name'],item['price'])
   
    print("                                        ")    
    print("========================================")
    print("Select the product you want to purchase ")
    print("========================================")
    selection()
    
    
# Selection page, select items from the Main page to be added to cart.   
def selection():        
    purchase = True
    while purchase == True:
        select = input(":").replace(':', '')
        purchase = False if not select else True
        if purchase:
            cart.append(item_db[int(select)-1])
    total_price = sum([item["price"] for item in cart])            
        
    print("==================")
    print("   Cart Summary  ")
    print("==================")
    for item in cart:
        print(item["name"])    
    print("                  ")
    print("                  ")
    print("==================")
    print(f"CHECKOUT = (GHc{total_price})")
    print("==================")    
        
        
    
    
   

def app():
    auth()




# Running app
app()
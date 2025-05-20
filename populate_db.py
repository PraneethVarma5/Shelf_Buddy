import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create products table
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    shelf_life_room_closed INTEGER,
    shelf_life_room_opened INTEGER,
    shelf_life_refrigerated_closed INTEGER,
    shelf_life_refrigerated_opened INTEGER,
    shelf_life_frozen_closed INTEGER,
    shelf_life_frozen_opened INTEGER
)
''')

# Sample food & medicine items
products = [
    ('Potatoes','Vegetables',21,'N/A',90,60,'N/A',0),
    ('Onions','Vegetables',60,45,90,60,0,0),
    ('Garlic','Vegetables',150,120,365,180,0,0),
    ('Carrots','Vegetables',3,2,14,10,365,240),
    ('Spinach','Vegetables',2,1,5,3,365,240),
    ('Tomatoes','Vegetables',21,14,0,0,60,45),

    ('Milk', 'food', 1, 0, 7, 3, 30, 15),
    ('Bread', 'food', 5, 2, 7, 3, 14, 7),
    ('Chicken', 'food', 1, 1, 2, 1, 180, 90),
    ('Rice', 'food', 365, 180, 730, 365, 1095, 730),
    ('Apple', 'food', 7, 4, 21, 10, 60, 30),
    ('Paracetamol', 'medicine', 730, 365, 1095, 730, 1460, 1095),
    ('Vitamin C', 'medicine', 365, 180, 730, 365, 1095, 730),
    ('Cough Syrup', 'medicine', 365, 90, 730, 180, 0, 0)
]

c.executemany('''
INSERT INTO products (
    name, category,
    shelf_life_room_closed, shelf_life_room_opened,
    shelf_life_refrigerated_closed, shelf_life_refrigerated_opened,
    shelf_life_frozen_closed, shelf_life_frozen_opened
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', products)

conn.commit()
conn.close()
print("Database populated.")

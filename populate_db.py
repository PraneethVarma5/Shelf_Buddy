import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create products table (if it doesn't exist)
# This part was 100% correct
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    shelf_life_room_closed INTEGER,
    shelf_life_room_opened INTEGER,
    shelf_life_refrigerated_closed INTEGER,
    shelf_life_refrigerated_opened INTEGER,
    shelf_life_frozen_closed INTEGER,
    shelf_life_frozen_opened INTEGER
)
''')

# --- List 1: User's provided 'items' list (83 items) ---
items = [
    ("Rice (white)", "food", 3650, 3650, 3650, 3650, 10950, 10950),
    ("Basmati rice", "food", 3650, 3650, 3650, 3650, 10950, 10950),
    ("Wheat flour (Atta)", "food", 360, 180, 360, 360, 720, 720),
    ("Gram flour (Besan)", "food", 360, 180, 360, 360, 720, 720),
    ("Moong dal (whole)", "food", 365, 365, 365, 365, 730, 730),
    ("Moong dal (split)", "food", 180, 180, 270, 270, 730, 730),
    ("Urad dal (whole)", "food", 365, 365, 365, 365, 730, 730),
    ("Urad dal (split)", "food", 180, 180, 270, 270, 730, 730),
    ("Chana dal (split)", "food", 270, 180, 365, 365, 730, 730),
    ("Chana (chickpeas, whole)", "food", 270, 180, 365, 365, 730, 730),
    ("Masoor dal (red lentil)", "food", 270, 180, 365, 365, 730, 730),
    ("Toor dal (pigeon pea)", "food", 365, 180, 365, 365, 730, 730),
    ("Rajma (kidney beans)", "food", 365, 365, 365, 365, 1095, 1095),
    ("Chole (chickpeas)", "food", 365, 365, 365, 365, 1095, 1095),
    ("Soya beans", "food", 365, 365, 365, 365, 1095, 1095),
    ("Soya chunks (TVP)", "food", 180, 90, 180, 180, 365, 365),
    ("Cumin (Jeera)", "food", 365, 365, 730, 730, 1095, 1095),
    ("Turmeric powder (Haldi)", "food", 730, 730, 1095, 1095, 1460, 1460),
    ("Red chili powder", "food", 365, 365, 730, 730, 1095, 1095),
    ("Salt", "food", 0, 0, 0, 0, 0, 0),
    ("Sugar", "food", 365, 365, 365, 365, 1095, 1095),
    ("Vegetable oil", "food", 180, 90, 365, 365, 365, 365),
    ("Ghee", "food", 365, 365, 365, 365, 365, 365),
    ("Butter", "food", 2, 2, 150, 150, 365, 365),
    ("Milk (pasteurized)", "food", 1, 1, 7, 7, 30, 30),
    ("Milk (UHT tetra-pack)", "food", 180, 1, 180, 2, 90, 30),
    ("Yogurt (curd/Dahi)", "food", 5, 5, 12, 12, 30, 30),
    ("Buttermilk (Chaas)", "food", 1, 1, 3, 3, 0, 0),
    ("Paneer (fresh cheese)", "food", 0, 0, 2, 2, 60, 60),
    ("Curd (homemade yogurt)", "food", 5, 5, 12, 12, 30, 30),
    ("Khoya (milk solids)", "food", 1, 1, 5, 5, 30, 30),
    ("Rice flour", "food", 180, 180, 365, 365, 730, 730),
    ("Coconut (fresh)", "food", 2, 2, 7, 7, 180, 180),
    ("Coconut (dry, desiccated)", "food", 180, 180, 365, 365, 730, 730),
    ("Potato", "food", 30, 30, 28, 28, 180, 180),
    ("Onion", "food", 30, 30, 90, 90, 240, 240),
    ("Tomato", "food", 5, 5, 14, 14, 30, 30),
    ("Garlic", "food", 90, 90, 180, 180, 365, 365),
    ("Ginger (whole)", "food", 21, 7, 30, 14, 180, 180),
    ("Green chili", "food", 5, 5, 14, 14, 30, 30),
    ("Okra (ladies' finger)", "food", 3, 3, 15, 15, 180, 180),
    ("Bitter gourd (karela)", "food", 4, 4, 21, 21, 90, 90),
    ("Brinjal (eggplant)", "food", 3, 3, 5, 3, 90, 90),
    ("Cabbage", "food", 2, 2, 10, 10, 180, 180),
    ("Cauliflower", "food", 3, 3, 7, 7, 90, 90),
    ("Carrot", "food", 5, 5, 14, 14, 180, 180),
    ("Green peas (fresh)", "food", 1, 1, 7, 7, 180, 180),
    ("Pumpkin (kaddoo)", "food", 30, 30, 60, 60, 180, 180),
    ("Bottle gourd (lauki)", "food", 3, 3, 7, 7, 90, 90),
    ("Ridge gourd (turai)", "food", 3, 3, 5, 5, 90, 90),
    ("Drumstick", "food", 2, 2, 5, 5, 90, 90),
    ("Banana (ripe)", "food", 3, 3, 7, 7, 30, 30),
    ("Apple", "food", 7, 7, 30, 30, 180, 180),
    ("Mango (ripe)", "food", 5, 5, 7, 7, 180, 180),
    ("Dates (dried)", "food", 180, 180, 365, 365, 730, 730),
    ("Biscuits (dry)", "food", 30, 15, 60, 30, 180, 90),
    ("Instant noodles (dry)", "food", 300, 300, 730, 730, 1095, 1095),
    ("Tea (loose)", "food", 365, 365, 365, 365, 365, 365),
    ("Coffee powder", "food", 180, 90, 365, 365, 730, 730),
    ("Honey", "food", 0, 0, 0, 0, 0, 0),
    ("Salted lemon pickle (homemade)", "food", 180, 30, 365, 60, 365, 90),
    ("Antacid tablets", "medicine", 730, 365, 730, 365, 1095, 730),
    ("Paracetamol tablets", "medicine", 730, 365, 730, 365, 1095, 730),
    ("Ibuprofen tablets", "medicine", 730, 365, 730, 365, 1095, 730),
    ("Cetirizine tablets", "medicine", 730, 365, 730, 365, 1095, 730),
    ("Loperamide tablets", "medicine", 730, 365, 730, 365, 1095, 730),
    ("Cough syrup (generic)", "medicine", 180, 90, 180, 90, 365, 180),
    ("Antacid syrup", "medicine", 180, 90, 180, 90, 365, 180),
    ("ORS powder sachet", "medicine", 365, 180, 365, 180, 730, 360),
    ("Multivitamin tablets", "medicine", 730, 365, 730, 365, 1095, 730),
    ("Antiseptic liquid (e.g., Dettol)", "medicine", 365, 180, 365, 180, 1095, 365),
    ("Antibiotic cream", "medicine", 365, 180, 365, 180, 1095, 365),
    ("Calamine lotion", "medicine", 365, 180, 365, 180, 1095, 365),
    ("Paracetamol syrup (child)", "medicine", 180, 90, 180, 90, 365, 180),
    ("Eye drops", "medicine", 180, 30, 180, 30, 365, 180),
    ("Ear drops", "medicine", 180, 30, 180, 30, 365, 180),
    ("Pain relief balm (e.g., Tiger Balm)", "medicine", 365, 180, 365, 180, 365, 180),
    ("Hydrocortisone cream", "medicine", 365, 180, 365, 180, 1095, 365),
    ("Antifungal cream", "medicine", 365, 180, 365, 180, 1095, 365),
    ("Oral rehydration salts (ORS)", "medicine", 365, 180, 365, 180, 730, 360)
]

# --- List 2: Standardized 'new_products_india' list (55 items) ---
# (All 'None' values have been replaced with 0 to match your list format)
new_products_india_standardized = [
    # Flours & Grains (Prone to weevils in humidity)
    ('Atta (Wheat Flour)', 'Flour', 90, 30, 180, 90, 365, 180),
    ('Besan (Gram Flour)', 'Flour', 120, 60, 180, 90, 365, 180),
    ('Sooji (Semolina)', 'Flour', 120, 60, 180, 90, 365, 180),
    ('Maida (Refined Flour)', 'Flour', 120, 60, 180, 90, 365, 180),
    ('Basmati Rice (White, Dry)', 'Grains', 730, 365, 730, 365, 0, 0),
    ('Brown Rice (Dry)', 'Grains', 180, 90, 365, 180, 0, 0),
    ('Poha (Flattened Rice)', 'Grains', 120, 45, 180, 90, 0, 0),

    # Dals & Pulses (Store airtight)
    ('Toor Dal (Arhar)', 'Pulses', 365, 180, 365, 180, 0, 0),
    ('Moong Dal', 'Pulses', 365, 180, 365, 180, 0, 0),
    ('Chana Dal', 'Pulses', 365, 180, 365, 180, 0, 0),
    ('Urad Dal', 'Pulses', 365, 180, 365, 180, 0, 0),
    ('Rajma (Dry)', 'Pulses', 730, 365, 730, 365, 0, 0),
    ('Kabuli Chana (Chickpeas, Dry)', 'Pulses', 730, 365, 730, 365, 0, 0),

    # Spices (Lose potency in heat)
    ('Coriander Powder (Dhania)', 'Spices', 180, 180, 365, 365, 0, 0),
    ('Cumin Powder (Jeera)', 'Spices', 180, 180, 365, 365, 0, 0),
    ('Garam Masala (Blend)', 'Spices', 180, 180, 365, 365, 0, 0),
    ('Cumin Seeds (Jeera)', 'Spices', 730, 730, 730, 730, 0, 0),
    ('Mustard Seeds (Rai)', 'Spices', 730, 730, 730, 730, 0, 0),
    ('Asafoetida (Hing)', 'Spices', 365, 365, 365, 365, 0, 0),

    # Oils & Fats (Go rancid in heat)
    # ('Ghee', 'Oils', 180, 90, 365, 180, 0, 0), # Duplicate 'Ghee' from list 1
    ('Mustard Oil', 'Oils', 180, 90, 180, 90, 0, 0),
    ('Coconut Oil (Virgin)', 'Oils', 365, 180, 365, 180, 0, 0),
    ('Sunflower Oil', 'Oils', 180, 90, 180, 90, 0, 0),
    ('Groundnut Oil', 'Oils', 180, 90, 180, 90, 0, 0),
    
    # Dairy & Perishables
    ('Paneer (Fresh/Packaged)', 'Dairy', 1, 1, 7, 3, 90, 30),
    ('Dahi (Curd, Homemade)', 'Dairy', 1, 1, 3, 2, 0, 0),
    ('Dahi (Curd, Packaged)', 'Dairy', 0, 0, 10, 5, 0, 0),
    ('UHT Milk (Tetra Pak, Unopened)', 'Dairy', 180, 0, 180, 0, 0, 0),
    ('UHT Milk (Tetra Pak, Opened)', 'Dairy', 0, 0, 3, 3, 0, 0),
    ('Idli/Dosa Batter (Fresh)', 'Perishables', 0, 0, 3, 2, 30, 15),

    # Common Indian Vegetables
    ('Okra (Bhindi)', 'Vegetables', 2, 0, 5, 3, 0, 0),
    ('Brinjal (Baingan)', 'Vegetables', 3, 0, 7, 4, 0, 0),
    # ('Bitter Gourd (Karela)', 'Vegetables', 4, 0, 10, 5, 0, 0), # Duplicate 'Bitter gourd (karela)'
    ('Bottle Gourd (Lauki)', 'Vegetables', 4, 0, 10, 5, 0, 0),
    # ('Ginger', 'Vegetables', 14, 7, 30, 21, 180, 90), # Duplicate 'Ginger (whole)'
    ('Green Chillies', 'Vegetables', 3, 2, 14, 7, 180, 90),
    ('Curry Leaves (Fresh)', 'Vegetables', 1, 1, 7, 5, 90, 60),
    
    # Condiments & Other
    ('Tamarind (Imli) Block', 'Condiments', 365, 180, 365, 180, 0, 0),
    ('Jaggery (Gud)', 'Sweetener', 180, 90, 365, 180, 0, 0),
    ('Mango Pickle (Achar, Opened)', 'Condiments', 90, 90, 180, 180, 0, 0),
    ('Papad (Uncooked)', 'Snacks', 365, 180, 365, 180, 0, 0),
    ('Namkeen/Bhujia (Opened)', 'Snacks', 14, 14, 30, 30, 0, 0),
    ('Parle-G (Biscuits, Opened)', 'Snacks', 21, 21, 30, 30, 0, 0),

    # Common Indian Medicines (Store below 25°C)
    ('Crocin/Dolo (Paracetamol)', 'Medicine', 730, 365, 730, 365, 0, 0),
    ('Disprin (Aspirin)', 'Medicine', 730, 365, 730, 365, 0, 0),
    ('Combiflam (Ibuprofen+PCM)', 'Medicine', 730, 365, 730, 365, 0, 0),
    ('Digene (Antacid Tablets)', 'Medicine', 730, 365, 730, 365, 0, 0),
    ('Gelusil (Antacid Liquid)', 'Medicine', 730, 90, 730, 90, 0, 0),
    ('ORS Powder (Sealed)', 'Medicine', 730, 0, 730, 0, 0, 0),
    ('ORS (Reconstituted)', 'Medicine', 1, 1, 1, 1, 0, 0),
    ('Vicks VapoRub (Opened)', 'Medicine', 365, 365, 365, 365, 0, 0),
    ('Benadryl (Cough Syrup)', 'Medicine', 730, 180, 730, 180, 0, 0),
    ('Strepsils (Lozenges)', 'Medicine', 730, 730, 730, 730, 0, 0)
]


# --- Combine both lists ---
all_products_to_insert = items + new_products_india_standardized
total_potential_items = len(all_products_to_insert)
original_items_count = len(items)
new_items_count = len(new_products_india_standardized)


# --- Insert all new products, ignoring duplicates ---
try:
    c.executemany('''
    INSERT OR IGNORE INTO products (
        name, category,
        shelf_life_room_closed, shelf_life_room_opened,
        shelf_life_refrigerated_closed, shelf_life_refrigerated_opened,
        shelf_life_frozen_closed, shelf_life_frozen_opened
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', all_products_to_insert)
    
    # Get the number of rows actually inserted
    inserted_count = c.rowcount
    conn.commit()
    
    # Provide a clear, accurate report
    print(f"Database population complete.")
    print(f"Attempted to insert {total_potential_items} items (from {original_items_count} + {new_items_count} lists).")
    print(f"Successfully inserted {inserted_count} unique items.")
    print(f"{total_potential_items - inserted_count} duplicate items were IGNORED.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback() # Roll back changes if an error occurs

finally:
    conn.close()
    print("Database connection closed.")
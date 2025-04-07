import sqlite3

con = sqlite3.connect("sqlite.db")
cur = con.cursor()

cur.execute("PRAGMA foreign_keys = ON")

cur.execute("""
            CREATE TABLE IF NOT EXISTS home_screen (
            id INTEGER PRIMARY KEY,
            bg_img TEXT, 
            reserve_status_text TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            INSERT INTO home_screen DEFAULT VALUES
            """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS guide_screen (
            id INTEGER PRIMARY KEY,
            bg_img TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE donate_screen (
            id INTEGER PRIMARY KEY,
            donate_text TEXT, 
            donation_website_link TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE emergency_screen (
            id INTEGER PRIMARY KEY,
            emergency_text_1 TEXT, 
            phone_number_1 TEXT, 
            emergency_text_2 TEXT, 
            phone_number_2 TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE safety_screen (
            id INTEGER PRIMARY KEY,
            bg_img TEXT, 
            safety_img TEXT, 
            safety_text TEXT, 
            emergency_contact_text TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE rules_screen (
            id INTEGER PRIMARY KEY,
            bg_img TEXT, 
            rules_img TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE rules (
            id INTEGER PRIMARY KEY,
            rule_img TEXT, 
            rule_text TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE about_screen (
            id INTEGER PRIMARY KEY,
            bg_img TEXT, 
            about_text TEXT, 
            reserve_website_link TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE share_screen (
            id INTEGER PRIMARY KEY,
            bg_img TEXT, 
            share_email TEXT, 
            share_phone_number TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE reports (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            phone_number TEXT, 
            email TEXT, 
            report_text TEXT, 
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE TABLE report_images (
            id INTEGER PRIMARY KEY, 
            report_id TEXT, 
            img TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(report_id) REFERENCES reports(id) ON DELETE CASCADE
            )""")

cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_report_id ON report_images(report_id)
            """)

cur.execute("""
            CREATE TABLE guide (
            id INTEGER PRIMARY KEY, 
            common_name TEXT, 
            latin_name TEXT, 
            img TEXT, 
            description TEXT, 
            color TEXT, 
            season TEXT, 
            class TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")

cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_guide_class ON guide(class)
            """)

con.commit()
con.close()
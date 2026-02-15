-- Create the Users table (FR-1)
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create the Reminders table (FR-3, FR-5)
CREATE TABLE IF NOT EXISTS reminders (
    reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    trigger_type TEXT, -- 'Availability', 'Specific Time', 'Working Hours'
    fallback_deadline DATETIME,
    status TEXT DEFAULT 'Pending', -- 'Pending', 'Triggered', 'Completed'
    actual_trigger_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

-- Create the Availability table (FR-6, FR-8)
CREATE TABLE IF NOT EXISTS availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    day_of_week TEXT NOT NULL, -- 'Monday', 'Tuesday', etc.
    start_time TEXT NOT NULL,  -- '09:00'
    end_time TEXT NOT NULL,    -- '12:00'
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);
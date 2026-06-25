# === Stage 63: Add relationships between records where useful ===
# Project: CraftFlow
from typing import Optional, List
import sqlite3

def link_records(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Link materials to projects (many-to-many via junction table if not exists)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS project_materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            material_id INTEGER NOT NULL,
            quantity REAL DEFAULT 1.0,
            FOREIGN KEY(project_id) REFERENCES projects(id),
            FOREIGN KEY(material_id) REFERENCES materials(id)
        )""")
    
    # Link milestones to projects (one-to-many)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS project_milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            milestone_name TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(project_id) REFERENCES projects(id)
        )""")
    
    # Link inspiration notes to projects or materials (many-to-many flexible)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS project_inspiration (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL CHECK(source_type IN ('project', 'material')),
            source_id INTEGER NOT NULL,
            note_text TEXT NOT NULL,
            FOREIGN KEY(source_id) REFERENCES projects(id),
            FOREIGN KEY(source_id) REFERENCES materials(id)
        )""")

    # Link costs to specific project phases or milestones (one-to-many)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS project_costs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            cost_category TEXT DEFAULT 'general',
            amount REAL NOT NULL,
            FOREIGN KEY(project_id) REFERENCES projects(id)
        )""")

    conn.commit()
    cur.close()
    conn.close()

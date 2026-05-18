# pyrefly: ignore [missing-import]
import frappe


def run(*args, **kwargs):
    print("\n--- Fixing Duplicate Students ---")
    
    new_names = [
        "Rahul", "Chandra", "Lily", "Priya", 
        "Siddharth", "Sai", "Amit", "Neha", 
        "Rohan", "Sneha", "Vikram", "Pooja", 
        "Aditya", "Riya", "Karan", "Anisha"
    ]
    
    try:
        # Get existing names to avoid creating new duplicates
        existing = frappe.db.sql("SELECT student_name FROM `tabStudent`", as_dict=True)
        existing_names = {str(r.get('student_name', '')).strip().lower() for r in existing if r.get('student_name')}
        
        # Filter available names
        available_names = [n for n in new_names if n.lower() not in existing_names]
        
        # Find all duplicates
        duplicates = frappe.db.sql("""
            SELECT student_name, GROUP_CONCAT(name) as doc_names 
            FROM `tabStudent` 
            GROUP BY student_name 
            HAVING COUNT(*) > 1
        """, as_dict=True)
        
        for row in duplicates:
            # The IDs of all students sharing the same name
            if not row.get('doc_names'):
                continue
            
            ids = str(row['doc_names']).split(',')
            
            # Keep the first one, rename the rest
            for i, doc_id in enumerate(ids[1:], start=2):
                if available_names:
                    new_name = available_names.pop(0)
                else:
                    new_name = f"{row.get('student_name', 'Student')} {i}"
                
                frappe.db.sql("UPDATE `tabStudent` SET student_name = %s WHERE name = %s", (new_name, doc_id))
                print(f"Renamed duplicate student (ID: {doc_id}) from '{row.get('student_name')}' to '{new_name}'")
                
        frappe.db.commit()
        print("--- Duplicate Fix Complete! ---\n")
    except Exception as e:
        print(f"Notice: Could not run duplicate fix. Error: {e}")


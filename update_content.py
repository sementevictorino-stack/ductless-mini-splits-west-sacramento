#!/usr/bin/env python3
"""
Script to update all HTML files with West Sacramento, CA localized content
"""

import os
import re
import glob

# Define replacement mappings
replacements = {
    # Basic location replacements - be more specific
    'Staten Island Ductless Mini Splits': 'West Sacramento Ductless Mini Splits',
    'Staten Island': 'West Sacramento',
    'statenislandductless.com': 'westsacramentoductless.com',
    'info@statenislandductless.com': 'info@westsacramentoductless.com',
    'SI Ductless Pro': 'WS Ductless Pro',
    
    # Address and geographic
    '123 Victory Blvd': '1500 West Capitol Avenue',
    'Staten Island, NY': 'West Sacramento, CA',
    ', NY': ', CA',
    ' NY': ' CA',
    'NY,': 'CA,',
    'NY.': 'CA.',
    'New York': 'California',
    
    # Zip codes
    '10301': '95691',
    '10302': '95691', 
    '10303': '95691',
    '10304': '95691',
    '10305': '95691',
    '10306': '95691',
    '10307': '95691',
    '10308': '95691',
    '10309': '95691',
    '10310': '95691',
    '10311': '95691',
    '10312': '95691',
    '10313': '95691',
    '10314': '95691',
    
    # Coordinates
    '40.6282': '38.5816',
    '-74.0776': '-121.5302',
    
    # Location names
    'St. George': 'Southport',
    'Stapleton': 'Bryte',
    'Port Richmond': 'Broderick', 
    'Tottenville': 'Downtown West Sacramento',
    'Great Kills': 'Riverfront District',
    'New Brighton': 'West Capitol Avenue',
    'West Brighton': 'Jefferson Boulevard',
    'South Beach': 'Industrial District',
    
    # Emergency banner specific to locations
    'Emergency HVAC Services Available in St. George': 'Emergency HVAC Services Available in West Sacramento',
    
    # Climate references
    'winter storm': 'rare winter cold snap',
    'summer heat wave': 'intense summer heat',
    
    # Reviews
    'Maria R., St. George': 'Maria R., Southport',
    'John D., Tottenville': 'John D., Bryte', 
    'Sarah L., Great Kills': 'Sarah L., Downtown',
    'Best HVAC company on Staten Island': 'Best HVAC company in West Sacramento'
}

def update_file_content(file_path):
    """Update a single file with the replacement mappings"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Apply all replacements
        for old_text, new_text in replacements.items():
            if old_text in content:
                content = content.replace(old_text, new_text)
                changes_made.append(f"  - {old_text} -> {new_text}")
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
            for change in changes_made:
                print(change)
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all HTML files
    html_files = []
    html_files.extend(glob.glob(os.path.join(script_dir, "*.html")))
    html_files.extend(glob.glob(os.path.join(script_dir, "services", "*.html")))
    html_files.extend(glob.glob(os.path.join(script_dir, "locations", "*.html")))
    
    print(f"Found {len(html_files)} HTML files to update")
    print("="*50)
    
    updated_count = 0
    for file_path in html_files:
        if update_file_content(file_path):
            updated_count += 1
        print("-"*30)
    
    print(f"\nCompleted! Updated {updated_count} out of {len(html_files)} files")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script to fix remaining NY -> CA and other specific issues
"""

import os
import glob

def fix_remaining_issues(file_path):
    """Fix remaining NY -> CA and other specific issues"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Specific fixes needed
        fixes = {
            '"addressRegion": "NY"': '"addressRegion": "CA"',
            'California Harbor': 'Sacramento River',
            'waterfront condos': 'riverfront condos',
            'home to the West Sacramento Ferry terminal': 'located along the Sacramento River',
            'Staten Island HVAC': 'West Sacramento HVAC',
            'Staten Island building codes': 'West Sacramento building codes',
            'Staten Island,': 'West Sacramento,',
            'Staten Island.': 'West Sacramento.',
            'Staten Island ': 'West Sacramento ',
            'Staten Island\'': 'West Sacramento\'',
            'Staten Island-': 'West Sacramento-',
            'Staten Island;': 'West Sacramento;',
            'Staten Island:': 'West Sacramento:',
            'Staten Island!': 'West Sacramento!',
            'Staten Island?': 'West Sacramento?',
            'serving Staten Island': 'serving West Sacramento',
            'throughout Staten Island': 'throughout West Sacramento',
            'in Staten Island': 'in West Sacramento',
            'on Staten Island': 'in West Sacramento',
            'across Staten Island': 'across West Sacramento',
            ', NY,': ', CA,',
            ' NY ': ' CA ',
            ' NY.': ' CA.',
            ' NY,': ' CA,',
            ' NY;': ' CA;',
            ' NY:': ' CA:',
            ' NY!': ' CA!',
            ' NY?': ' CA?',
            'NY zip codes': 'CA neighborhoods',
            'New York state': 'California',
            'waterfront air quality': 'air quality during wildfire season',
            'salt air corrosion': 'dust and heat exposure',
            'winter storms': 'rare winter cold snaps',
            'humid summers': 'hot, dry summers',
            'cold winters': 'mild winters'
        }
        
        # Apply fixes
        for old_text, new_text in fixes.items():
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
            return False
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to fix remaining issues in all HTML files"""
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all HTML files
    html_files = []
    html_files.extend(glob.glob(os.path.join(script_dir, "*.html")))
    html_files.extend(glob.glob(os.path.join(script_dir, "services", "*.html")))
    html_files.extend(glob.glob(os.path.join(script_dir, "locations", "*.html")))
    
    print(f"Found {len(html_files)} HTML files to check")
    print("="*50)
    
    updated_count = 0
    for file_path in html_files:
        if fix_remaining_issues(file_path):
            updated_count += 1
        else:
            print(f"No changes needed: {file_path}")
        print("-"*30)
    
    print(f"\nCompleted! Updated {updated_count} out of {len(html_files)} files")

if __name__ == "__main__":
    main()

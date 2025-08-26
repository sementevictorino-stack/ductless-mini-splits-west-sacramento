#!/usr/bin/env python3
"""
Final verification script to check all transformations
"""

import os
import glob
import re

def verify_transformations(file_path):
    """Verify that all major transformations have been applied"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # Check for remaining Staten Island references
        if 'Staten Island' in content:
            matches = re.findall(r'Staten Island[^>]*', content)
            issues.append(f"Still contains 'Staten Island': {matches[:3]}")  # Show first 3 matches
        
        # Check for NY state references that should be CA
        if ', NY' in content or ' NY ' in content:
            matches = re.findall(r'[^>]*\bNY\b[^<]*', content)
            issues.append(f"Still contains NY references: {matches[:3]}")
        
        # Check for old zip codes
        old_zips = ['10301', '10302', '10303', '10304', '10305', '10306', '10307', '10308', '10309', '10310', '10311', '10312', '10313', '10314']
        for old_zip in old_zips:
            if old_zip in content:
                issues.append(f"Still contains old zip code: {old_zip}")
                break
        
        # Check for old address
        if '123 Victory Blvd' in content:
            issues.append("Still contains old address: 123 Victory Blvd")
        
        # Check for old coordinates
        if '40.6282' in content or '-74.0776' in content:
            issues.append("Still contains old coordinates")
        
        # Verify West Sacramento content exists
        if 'West Sacramento' not in content:
            issues.append("Missing 'West Sacramento' references")
        
        return issues
        
    except Exception as e:
        return [f"Error reading file: {e}"]

def main():
    """Main function to verify all HTML files"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    html_files = []
    html_files.extend(glob.glob(os.path.join(script_dir, "*.html")))
    html_files.extend(glob.glob(os.path.join(script_dir, "services", "*.html")))
    html_files.extend(glob.glob(os.path.join(script_dir, "locations", "*.html")))
    
    print(f"Verifying {len(html_files)} HTML files...")
    print("="*70)
    
    total_issues = 0
    files_with_issues = 0
    
    for file_path in html_files:
        relative_path = os.path.relpath(file_path, script_dir)
        issues = verify_transformations(file_path)
        
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            print(f"\n❌ {relative_path}")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"✅ {relative_path}")
    
    print("\n" + "="*70)
    print(f"SUMMARY:")
    print(f"Total files checked: {len(html_files)}")
    print(f"Files with issues: {files_with_issues}")
    print(f"Files successfully updated: {len(html_files) - files_with_issues}")
    print(f"Total issues found: {total_issues}")
    
    if files_with_issues == 0:
        print("\n🎉 ALL FILES SUCCESSFULLY UPDATED!")
    else:
        print(f"\n⚠️  {files_with_issues} files still need attention")

if __name__ == "__main__":
    main()

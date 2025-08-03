#!/usr/bin/env python3
"""
Quick Project Updater
This script quickly updates your GitHub profile projects
"""

import sys
import os

# Add current directory to path to import fetch_github_repos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetch_github_repos import update_readme_projects

def main():
    """Quick project updater"""
    print("🚀 Quick GitHub Projects Updater")
    print("=" * 40)
    
    # Get username from command line or input
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Enter your GitHub username: ").strip()
    
    if not username:
        print("❌ Username is required!")
        return
    
    print(f"🔄 Updating projects for {username}...")
    
    # Update projects (without token for simplicity)
    if update_readme_projects(username):
        print("\n✅ Projects updated successfully!")
        print("📝 Next steps:")
        print("1. Review the changes in README.md")
        print("2. Commit and push to GitHub")
        print("3. Your profile will show your actual projects!")
    else:
        print("\n❌ Failed to update projects.")

if __name__ == "__main__":
    main() 
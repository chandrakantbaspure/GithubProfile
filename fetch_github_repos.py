#!/usr/bin/env python3
"""
GitHub Repository Fetcher and Profile Updater
This script fetches your GitHub repositories and updates your profile README
"""

import requests
import re
import os
from typing import List, Dict

def get_github_repositories(username: str, token: str = None) -> List[Dict]:
    """Fetch repositories from GitHub API"""
    
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    # Fetch public repositories
    url = f"https://api.github.com/users/{username}/repos"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        repos = response.json()
        
        # Filter and sort repositories
        java_repos = []
        other_repos = []
        
        for repo in repos:
            if not repo['fork']:  # Only include original repositories
                repo_info = {
                    'name': repo['name'],
                    'description': repo['description'] or f"A {repo['language'] or 'software'} project",
                    'language': repo['language'],
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'url': repo['html_url'],
                    'topics': repo.get('topics', [])
                }
                
                # Prioritize Java repositories
                if repo['language'] and 'java' in repo['language'].lower():
                    java_repos.append(repo_info)
                else:
                    other_repos.append(repo_info)
        
        # Sort by stars and combine
        java_repos.sort(key=lambda x: x['stars'], reverse=True)
        other_repos.sort(key=lambda x: x['stars'], reverse=True)
        
        return java_repos + other_repos[:5]  # Return top Java repos + 5 other repos
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching repositories: {e}")
        return []

def generate_project_section(repos: List[Dict], username: str) -> str:
    """Generate the projects section for README"""
    
    if not repos:
        return ""
    
    # Take top 4 repositories
    top_repos = repos[:4]
    
    project_sections = []
    
    for i, repo in enumerate(top_repos):
        # Determine emoji based on repository type
        emoji = "🚀"
        if any(keyword in repo['name'].lower() for keyword in ['api', 'service', 'backend']):
            emoji = "🔧"
        elif any(keyword in repo['name'].lower() for keyword in ['web', 'frontend', 'ui']):
            emoji = "🌐"
        elif any(keyword in repo['name'].lower() for keyword in ['mobile', 'app']):
            emoji = "📱"
        elif any(keyword in repo['name'].lower() for keyword in ['data', 'ml', 'ai']):
            emoji = "🤖"
        elif any(keyword in repo['name'].lower() for keyword in ['tool', 'util']):
            emoji = "🛠️"
        
        # Generate project description
        description = repo['description']
        if repo['language']:
            description += f" Built with {repo['language']}."
        
        # Add tech stack hints based on topics
        if repo['topics']:
            tech_stack = [topic for topic in repo['topics'] if topic not in ['java', 'spring', 'web', 'api']]
            if tech_stack:
                description += f" Uses {', '.join(tech_stack[:3])}."
        
        # Create project section
        project_section = f"""    <td width="50%">
      <h3 align="center">{emoji} {repo['name'].replace('-', ' ').replace('_', ' ').title()}</h3>
      <div align="center">
        <a href="{repo['url']}" target="_blank">
          <img src="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={repo['name']}&theme=radical&hide_border=true&bg_color=0D1117&title_color=6366F1&text_color=FFFFFF" width="100%" alt="{repo['name']}"/>
        </a>
      </div>
      <p align="center">
        {description}
      </p>
      <p align="center">
        <a href="{repo['url']}" target="_blank">
          <img src="https://img.shields.io/badge/Code-000000?style=for-the-badge&logo=github&logoColor=white" alt="View Code"/>
        </a>"""
        
        # Add live demo link if it's a web project
        if any(keyword in repo['name'].lower() for keyword in ['web', 'app', 'site', 'demo']):
            project_section += f"""
        <a href="https://{repo['name']}.vercel.app" target="_blank">
          <img src="https://img.shields.io/badge/Live_Demo-6366F1?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Demo"/>
        </a>"""
        
        project_section += """
      </p>
    </td>"""
        
        project_sections.append(project_section)
    
    # Create table structure
    table_rows = []
    for i in range(0, len(project_sections), 2):
        row = "  <tr>\n"
        row += project_sections[i]
        if i + 1 < len(project_sections):
            row += "\n" + project_sections[i + 1]
        row += "\n  </tr>"
        table_rows.append(row)
    
    return "\n".join(table_rows)

def update_readme_projects(username: str, token: str = None) -> bool:
    """Update the projects section in README.md"""
    
    if not os.path.exists('README.md'):
        print("❌ README.md not found! Please make sure you're in the correct directory.")
        return False
    
    print(f"🔍 Fetching repositories for {username}...")
    repos = get_github_repositories(username, token)
    
    if not repos:
        print("❌ No repositories found or error occurred.")
        return False
    
    print(f"✅ Found {len(repos)} repositories")
    
    # Generate new projects section
    new_projects_section = generate_project_section(repos, username)
    
    if not new_projects_section:
        print("❌ Failed to generate projects section.")
        return False
    
    # Read current README
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find and replace the projects table
    pattern = r'<table>.*?</table>'
    new_table = f"<table>\n{new_projects_section}\n</table>"
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_table, content, flags=re.DOTALL)
    else:
        print("❌ Could not find projects table in README.md")
        return False
    
    # Write updated README
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("✅ Projects section updated successfully!")
    print(f"\n📋 Updated projects:")
    for repo in repos[:4]:
        print(f"  - {repo['name']}: {repo['description']}")
    
    return True

def main():
    """Main function"""
    print("🚀 GitHub Repository Fetcher and Profile Updater")
    print("=" * 50)
    
    username = input("Enter your GitHub username: ").strip()
    
    # Optional GitHub token for higher rate limits
    use_token = input("Do you have a GitHub personal access token? (y/n): ").strip().lower()
    token = None
    
    if use_token == 'y':
        token = input("Enter your GitHub personal access token: ").strip()
        if not token:
            print("⚠️  No token provided, using public API (limited requests)")
    
    if update_readme_projects(username, token):
        print("\n🎉 Your GitHub profile projects have been updated!")
        print("📝 Don't forget to commit and push your changes to GitHub.")
    else:
        print("\n❌ Failed to update projects section.")

if __name__ == "__main__":
    main() 
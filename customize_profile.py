#!/usr/bin/env python3
"""
GitHub Profile Customization Script
This script helps you quickly customize your GitHub profile README.md
"""

import re
import os

def get_user_input():
    """Get user information for profile customization"""
    print("🚀 GitHub Profile Customization Tool")
    print("=" * 50)
    
    user_info = {}
    
    user_info['name'] = input("Enter your full name: ").strip()
    user_info['username'] = input("Enter your GitHub username: ").strip()
    user_info['email'] = input("Enter your email address: ").strip()
    user_info['title'] = input("Enter your professional title (e.g., Full Stack Developer): ").strip()
    user_info['location'] = input("Enter your location (optional, press Enter to skip): ").strip()
    user_info['portfolio'] = input("Enter your portfolio website URL (optional, press Enter to skip): ").strip()
    user_info['linkedin'] = input("Enter your LinkedIn profile URL (optional, press Enter to skip): ").strip()
    user_info['twitter'] = input("Enter your Twitter profile URL (optional, press Enter to skip): ").strip()
    user_info['devto'] = input("Enter your Dev.to profile URL (optional, press Enter to skip): ").strip()
    user_info['medium'] = input("Enter your Medium profile URL (optional, press Enter to skip): ").strip()
    user_info['spotify'] = input("Enter your Spotify username (optional, press Enter to skip): ").strip()
    
    return user_info

def customize_readme(user_info):
    """Customize the README.md file with user information"""
    
    if not os.path.exists('README.md'):
        print("❌ README.md not found! Please make sure you're in the correct directory.")
        return False
    
    # Read the current README
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace placeholders with user information
    replacements = {
        r'\[Your Name\]': user_info['name'],
        r'yourusername': user_info['username'],
        r'your\.email@example\.com': user_info['email'],
        r'Full Stack Developer': user_info['title'],
        r'your-spotify-username': user_info['spotify'] if user_info['spotify'] else 'your-spotify-username',
        r'your-portfolio\.com': user_info['portfolio'] if user_info['portfolio'] else 'your-portfolio.com',
        r'https://linkedin\.com/in/yourusername': user_info['linkedin'] if user_info['linkedin'] else 'https://linkedin.com/in/yourusername',
        r'https://twitter\.com/yourusername': user_info['twitter'] if user_info['twitter'] else 'https://twitter.com/yourusername',
        r'https://dev\.to/yourusername': user_info['devto'] if user_info['devto'] else 'https://dev.to/yourusername',
        r'https://medium\.com/@yourusername': user_info['medium'] if user_info['medium'] else 'https://medium.com/@yourusername',
    }
    
    # Apply replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Add location if provided
    if user_info['location']:
        location_pattern = r'(I\'m a passionate \*\*.*?\*\* with a love for)'
        location_replacement = f"\\1 creating innovative solutions from {user_info['location']} and"
        content = re.sub(location_pattern, location_replacement, content)
    
    # Write the customized README
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(content)
    
    return True

def get_tech_stack():
    """Get user's tech stack"""
    print("\n🛠️  Tech Stack Customization")
    print("=" * 30)
    
    categories = {
        'Backend & Core Java': ['Java', 'Spring Boot', 'Spring Framework', 'Spring Security', 'Spring Data JPA', 'Maven', 'Gradle', 'JUnit', 'Mockito'],
        'Frontend': ['React', 'Angular', 'TypeScript', 'JavaScript', 'HTML5', 'CSS3', 'Bootstrap', 'Thymeleaf'],
        'Database & ORM': ['MySQL', 'PostgreSQL', 'Oracle', 'Redis', 'Hibernate', 'JPA', 'MyBatis'],
        'DevOps & Cloud': ['Docker', 'Kubernetes', 'AWS', 'Azure', 'Jenkins', 'Maven', 'Gradle', 'Git', 'GitHub'],
        'Tools & IDEs': ['IntelliJ IDEA', 'Eclipse', 'VS Code', 'Postman', 'Swagger', 'Jira', 'Confluence']
    }
    
    selected_tech = {}
    
    for category, technologies in categories.items():
        print(f"\n{category} Technologies:")
        for i, tech in enumerate(technologies, 1):
            print(f"  {i}. {tech}")
        
        while True:
            try:
                choice = input(f"\nSelect {category} technologies (comma-separated numbers, or 'all' for all): ").strip()
                if choice.lower() == 'all':
                    selected_tech[category] = technologies
                    break
                elif choice:
                    indices = [int(x.strip()) - 1 for x in choice.split(',')]
                    selected_tech[category] = [technologies[i] for i in indices if 0 <= i < len(technologies)]
                    break
                else:
                    selected_tech[category] = []
                    break
            except (ValueError, IndexError):
                print("❌ Invalid input. Please try again.")
    
    return selected_tech

def generate_tech_badges(tech_stack):
    """Generate tech stack badges"""
    badge_templates = {
        # Backend & Core Java
        'Java': '![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)',
        'Spring Boot': '![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)',
        'Spring Framework': '![Spring Framework](https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white)',
        'Spring Security': '![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=spring-security&logoColor=white)',
        'Spring Data JPA': '![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-6DB33F?style=for-the-badge&logo=spring&logoColor=white)',
        'Maven': '![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apache-maven&logoColor=white)',
        'Gradle': '![Gradle](https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white)',
        'JUnit': '![JUnit](https://img.shields.io/badge/JUnit-25A162?style=for-the-badge&logo=junit5&logoColor=white)',
        'Mockito': '![Mockito](https://img.shields.io/badge/Mockito-78A641?style=for-the-badge&logo=mockito&logoColor=white)',
        
        # Frontend
        'React': '![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)',
        'Angular': '![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)',
        'TypeScript': '![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)',
        'JavaScript': '![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)',
        'HTML5': '![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)',
        'CSS3': '![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)',
        'Bootstrap': '![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)',
        'Thymeleaf': '![Thymeleaf](https://img.shields.io/badge/Thymeleaf-005F0F?style=for-the-badge&logo=thymeleaf&logoColor=white)',
        
        # Database & ORM
        'MySQL': '![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)',
        'PostgreSQL': '![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)',
        'Oracle': '![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)',
        'Redis': '![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)',
        'Hibernate': '![Hibernate](https://img.shields.io/badge/Hibernate-59666C?style=for-the-badge&logo=hibernate&logoColor=white)',
        'JPA': '![JPA](https://img.shields.io/badge/JPA-59666C?style=for-the-badge&logo=hibernate&logoColor=white)',
        'MyBatis': '![MyBatis](https://img.shields.io/badge/MyBatis-000000?style=for-the-badge&logo=mybatis&logoColor=white)',
        
        # DevOps & Cloud
        'Docker': '![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)',
        'Kubernetes': '![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)',
        'AWS': '![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)',
        'Azure': '![Azure](https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)',
        'Jenkins': '![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)',
        'Git': '![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)',
        'GitHub': '![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)',
        
        # Tools & IDEs
        'IntelliJ IDEA': '![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ_IDEA-000000?style=for-the-badge&logo=intellij-idea&logoColor=white)',
        'Eclipse': '![Eclipse](https://img.shields.io/badge/Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white)',
        'VS Code': '![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)',
        'Postman': '![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)',
        'Swagger': '![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=white)',
        'Jira': '![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)',
        'Confluence': '![Confluence](https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white)'
    }
    
    badge_sections = []
    
    for category, technologies in tech_stack.items():
        if technologies:
            badges = []
            for tech in technologies:
                if tech in badge_templates:
                    badges.append(badge_templates[tech])
            
            if badges:
                section = f"### {category}\n" + " ".join(badges)
                badge_sections.append(section)
    
    return "\n\n".join(badge_sections)

def main():
    """Main function"""
    try:
        # Get user information
        user_info = get_user_input()
        
        # Customize README
        if customize_readme(user_info):
            print("\n✅ README.md customized successfully!")
        else:
            print("\n❌ Failed to customize README.md")
            return
        
        # Get tech stack
        tech_stack = get_tech_stack()
        
        # Generate tech badges
        tech_badges = generate_tech_badges(tech_stack)
        
        # Save tech badges to a file for easy copying
        with open('tech_badges.md', 'w', encoding='utf-8') as file:
            file.write(tech_badges)
        
        print("\n✅ Tech stack badges generated and saved to 'tech_badges.md'")
        print("\n📋 Next Steps:")
        print("1. Copy the content from 'tech_badges.md' and replace the tech stack section in README.md")
        print("2. Update your project information in the 'Featured Projects' section")
        print("3. Customize the 'About Me' and 'Current Focus' sections")
        print("4. Commit and push your changes to GitHub")
        print("5. Your profile will be live at https://github.com/" + user_info['username'])
        
        print(f"\n🎉 Your GitHub profile is ready to be customized!")
        
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main() 
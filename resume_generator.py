import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Load JSON data
with open('resume.json', 'r') as f:
    data = json.load(f)

# Create PDF
name = data['personal_information']['name'].replace(' ', '_')
date_str = datetime.now().strftime('%d%m%y')
pdf_filename = f"{name}_resume_{date_str}.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
elements = []

# Styles
styles = getSampleStyleSheet()
style_title = styles['Title']
style_heading = styles['Heading2']
style_normal = styles['Normal']
style_normal.leading = 14  # Adjust line spacing

# Helper function to add paragraphs
def add_paragraph(text, style):
    elements.append(Paragraph(text, style))
    elements.append(Spacer(1, 8))

# Header
add_paragraph(data['personal_information']['name'], style_title)
contact_info = f"$ {data['personal_information']['mobile']}   {data['personal_information']['email']}<br/>" \
               f"linkedin.com/{data['personal_information']['linkedin'].split('/')[-1]}   github.com/{data['personal_information']['github'].split('/')[-1]}"
add_paragraph(contact_info, style_normal)

# Education
add_paragraph("Education", style_heading)
for edu in data['education']:
    edu_text = f"{edu['institution']}<br/>{edu['degree']} (CGPA: {edu.get('cgpa', 'N/A')})<br/>Expected - {edu['expected_graduation']}<br/>{edu.get('location', '')}"
    add_paragraph(edu_text, style_normal)

# Experience
add_paragraph("Experience", style_heading)
for exp in data['experience']:
    exp_text = f"{exp['organization']}<br/>{exp['role']}<br/>{exp['duration']}"
    add_paragraph(exp_text, style_normal)
    for resp in exp['responsibilities']:
        add_paragraph(f"• {resp}", style_normal)

# Projects
add_paragraph("Projects", style_heading)
for project in data['projects']:
    project_text = f"{project['title']}<br/>Github: {project.get('github', 'N/A')}<br/>{project['description'].split('.')[0]}"
    add_paragraph(project_text, style_normal)
    for desc in project['description'].split('.')[1:]:
        if desc.strip():
            add_paragraph(f"• {desc.strip()}", style_normal)

# Technical Skills
add_paragraph("Technical Skills", style_heading)
skills_text = f"Languages: {', '.join(data['technical_skills']['languages'])}<br/>" \
              f"Technologies: {', '.join(data['technical_skills']['technologies'])}<br/>" \
              f"Database Systems: {', '.join(data['technical_skills']['database_systems'])}<br/>" \
              f"DevOps / Cloud: {', '.join(data['technical_skills']['devops_cloud'])}<br/>" \
              f"Tools: {', '.join(data['technical_skills']['tools'])}"
add_paragraph(skills_text, style_normal)

# Achievements
if 'achievements' in data:
    add_paragraph("Achievements", style_heading)
    for achievement in data['achievements']:
        ach_text = f"{achievement['title']}<br/>Project: {achievement.get('project', 'N/A')}<br/>{achievement.get('link', 'N/A')}"
        add_paragraph(ach_text, style_normal)
        add_paragraph(f"• {achievement['description']}", style_normal)

# Position of Responsibility
if 'position_of_responsibility' in data:
    add_paragraph("Position of Responsibility", style_heading)
    for pos in data['position_of_responsibility']:
        pos_text = f"{pos['organization']}<br/>{pos.get('location', 'N/A')}<br/>{pos['role']}<br/>{pos['duration']}"
        add_paragraph(pos_text, style_normal)
        add_paragraph(f"• {pos['description']}", style_normal)

# Build PDF
doc.build(elements)

import json
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_resume(input_file):
    with open(input_file, "r") as file:
        data = json.load(file)

    # Generate filename with current date in ddmmyy format
    date_str = datetime.datetime.now().strftime("%d%m%y")
    output_file = f"{data['name'].split()[0]}_resume_{date_str}.pdf"

    c = canvas.Canvas(output_file, pagesize=letter)
    # (Resume content code remains the same)
    c.save()

    return output_file  # ❌ No print statement here!

    # Name and Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, y_position, data["name"])
    y_position -= 30
    c.setFont("Helvetica", 14)
    c.drawString(40, y_position, data["title"])
    y_position -= 40

    # Contact Info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y_position, "Contact:")
    y_position -= 20
    c.setFont("Helvetica", 12)
    c.drawString(40, y_position, f"Email: {data['contact']['email']}")
    y_position -= 20
    c.drawString(40, y_position, f"Phone: {data['contact']['phone']}")
    y_position -= 20
    c.drawString(40, y_position, f"LinkedIn: {data['contact']['linkedin']}")
    y_position -= 40

    # Skills
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y_position, "Skills:")
    y_position -= 20
    c.setFont("Helvetica", 12)
    c.drawString(40, y_position, ", ".join(data["skills"]))
    y_position -= 40

    # Experience
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y_position, "Experience:")
    y_position -= 20
    for job in data["experience"]:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y_position, f"{job['role']} at {job['company']} ({job['duration']})")
        y_position -= 20
        c.setFont("Helvetica", 12)
        c.drawString(40, y_position, job["description"])
        y_position -= 40

    # Education
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y_position, "Education:")
    y_position -= 20
    c.setFont("Helvetica", 12)
    c.drawString(40, y_position, f"{data['education']['degree']}, {data['education']['college']} ({data['education']['year']})")
    y_position -= 40

    # Projects
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y_position, "Projects:")
    y_position -= 20
    for project in data["projects"]:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y_position, f"{project['title']}")
        y_position -= 20
        c.setFont("Helvetica", 12)
        c.drawString(40, y_position, project["description"])
        y_position -= 20
        c.drawString(40, y_position, f"GitHub: {project['repo']}")
        y_position -= 40

    c.save()
    print(f"Resume saved as {output_file}")
    return output_file

# Run the script
generate_resume("resume.json")

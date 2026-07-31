from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def create_pdf(report, filename="financial_report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Financial Report</b>", styles["Heading1"]))

    story.append(Paragraph(report.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    return filename
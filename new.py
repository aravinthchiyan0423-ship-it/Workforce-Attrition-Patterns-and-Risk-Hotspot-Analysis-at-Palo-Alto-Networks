from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

file_path = "Mission_Dev_Interview_Preparation.pdf"
c = canvas.Canvas(file_path, pagesize=letter)

width, height = letter
text = c.beginText(40, height - 40)
text.setFont("Helvetica", 10)

content = """
Mission.dev - Junior Data Transformation Analyst Interview Prep

1. Tell me about yourself
Hi, I am an aspiring Data Analyst with skills in Excel, SQL, Python.
I enjoy working with data, cleaning, analyzing, and generating insights.

2. Why Mission.dev
I want to work on global client projects and data transformation tasks.

3. Excel Skills
Pivot Tables, XLOOKUP, VLOOKUP, INDEX-MATCH, IF, SUMIFS, COUNTIFS.

4. Data Accuracy
Validate source data, check duplicates, reconcile datasets, verify results.

5. Handling mismatched data
Compare datasets, identify differences using lookup functions, correct errors.

6. US Shift
Yes, I am comfortable working US Eastern Time.

7. Why should we hire you
I am detail-oriented, analytical, and strong in Excel, SQL, and Python.

Question 1: Tell me about yourself

Answer:

"Hello, my name is [Your Name], and I'm from Tamil Nadu, India. I have a strong interest in data analytics and enjoy working with data to solve business problems. I have experience using Excel, SQL, and Python for data cleaning, analysis, and reporting. I'm detail-oriented, enjoy working with large datasets, and always focus on maintaining data accuracy. I'm excited about this opportunity because it aligns well with my skills and my goal of building a career in data analytics."

🎥 Question 2: Why do you want to join Mission.dev?

Answer:

"I'm interested in Mission.dev because it offers the opportunity to work on global client projects and gain experience in data transformation and client onboarding. I enjoy working with data, solving problems, and improving data quality. This role will help me grow professionally while contributing to meaningful business outcomes."

🎥 Question 3: Explain your Excel skills.

Answer:

"I'm comfortable using Excel for data analysis and reporting. I have experience with Pivot Tables, XLOOKUP, VLOOKUP, INDEX-MATCH, IF, SUMIFS, COUNTIFS, Conditional Formatting, and data validation. I can compare large datasets, identify missing values and duplicates, and create reports that support business decisions."

🎥 Question 4: How do you ensure data accuracy?

Answer:

"I first validate the source data, check for missing or duplicate records, compare imported data with the original dataset, and use Excel functions to reconcile differences. I also perform quality checks before finalizing reports to ensure the information is accurate and reliable."

🎥 Question 5: Tell us about a challenge you solved.

Answer:

"While working on a dataset, I found inconsistencies between two reports. I compared the data using lookup functions, identified the mismatched records, corrected the errors, and verified the final output. This helped improve the accuracy of the report before it was shared."

🎥 Question 6: Are you comfortable working the US shift?

Answer:

"Yes. I'm comfortable working US Eastern Time hours and understand the importance of collaborating with global teams during their business hours."

🎥 Question 7: Why should we hire you?

Answer:

"I'm analytical, detail-oriented, and committed to delivering accurate work. I learn new tools quickly, communicate effectively, and enjoy solving data-related problems. I believe my Excel, SQL, and Python skills, combined with my willingness to learn, will help me contribute effectively to the team."

🔥 Technical Questions
Q: Difference between XLOOKUP and VLOOKUP?

Answer:

"VLOOKUP searches only from left to right, while XLOOKUP can search in any direction, returns exact matches by default, and is more flexible."

Q: What would you do if two datasets don't match?

Answer:

"I would compare key columns, identify missing or duplicate records, verify data sources, use lookup functions to find differences, and validate the corrected data before reporting."

Q: Have you worked with large datasets?

Answer:

"Yes. I'm comfortable using filters, Pivot Tables, lookup functions, and SQL to analyze and reconcile large datasets while maintaining accuracy."
"""

for line in content.split("\n"):
    text.textLine(line)

c.drawText(text)
c.save()

print("PDF created successfully!")
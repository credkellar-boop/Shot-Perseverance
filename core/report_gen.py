import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime

class ShotPerseveranceReport:
    def __init__(self, session_id):
        self.session_id = session_id
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        
    def create_shot_chart(self, actions):
        """
        Generates a 2D plot of the court with color-coded success markers.
        """
        plt.figure(figsize=(10, 8))
        # Draw a basic half-court outline
        plt.plot([0, 100], [0, 0], color="black") # Baseline
        plt.plot([50], [10], 'ro') # The Rim
        
        for act in actions:
            color = 'green' if act['score'] > 85 else 'orange' if act['score'] > 70 else 'red'
            plt.scatter(act['x'], act['y'], c=color, s=100, edgecolors='black')
            plt.text(act['x']+1, act['y']+1, act['type'], fontsize=9)

        chart_path = f"data/reports/chart_{self.session_id}.png"
        plt.savefig(chart_path)
        plt.close()
        return chart_path

    def generate_pdf(self, player_name, actions):
        chart_path = self.create_shot_chart(actions)
        
        self.pdf.add_page()
        # Header
        self.pdf.set_font("Arial", 'B', 20)
        self.pdf.cell(0, 10, f"SCOUTING REPORT: {player_name}", ln=True, align='C')
        self.pdf.set_font("Arial", '', 12)
        self.pdf.cell(0, 10, f"Date: {datetime.date.today()} | Session ID: {self.session_id}", ln=True, align='C')
        self.pdf.ln(10)

        # Insert Shot Chart
        self.pdf.image(chart_path, x=10, w=190)
        self.pdf.ln(5)

        # Action Breakdown Table
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(40, 10, "Action", 1)
        self.pdf.cell(40, 10, "Perfection %", 1)
        self.pdf.cell(60, 10, "Key Metric", 1)
        self.pdf.cell(50, 10, "Result", 1, ln=True)

        self.pdf.set_font("Arial", '', 10)
        for act in actions:
            self.pdf.cell(40, 10, act['type'], 1)
            self.pdf.cell(40, 10, f"{act['score']}%", 1)
            self.pdf.cell(60, 10, act['metric_detail'], 1)
            self.pdf.cell(50, 10, "EXCELLENT" if act['score'] > 85 else "WORK NEEDED", 1, ln=True)

        report_path = f"data/reports/report_{self.session_id}.pdf"
        self.pdf.output(report_path)
        return report_path

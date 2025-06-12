import telebot
import requests
import schedule
import time
from fpdf import FPDF
from datetime import datetime

# Telegram bot token
BOT_TOKEN = "7835822489:AAHrSYus2CR-BGtAdMisZARcwNVZtcT5bgU"
bot = telebot.TeleBot(BOT_TOKEN)

# Sample skills and experience keywords
KEYWORDS = ["logistics", "accounting", "software", "entry level", "remote", "field assistant"]

# Job sites to scan (placeholder)
JOB_SITES = [
    "https://jobs.lenoma.co.ke/",
    "https://fuzu.com/jobs",
    "https://kenyanjob.com"
]

# Function to simulate job scraping
def fetch_jobs():
    jobs = []
    for site in JOB_SITES:
        jobs.append({
            "title": "Junior Logistics Assistant",
            "company": "AgriTech Ltd",
            "location": "Kisumu",
            "link": "https://example.com/job123"
        })
    return jobs

# Generate application PDF
def generate_pdf(job):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Job Application", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"Applying for: {job['title']} at {job['company']}")
    pdf.multi_cell(0, 10, f"Location: {job['location']}")
    pdf.multi_cell(0, 10, f"Applicant: Patterson Olindi\nEmail: pattersonolindi@gmail.com\nExperience: 1 year at One Acre Fund")
    filename = f"{job['title'].replace(' ', '_')}.pdf"
    pdf.output(filename)
    return filename

# Job recommendation routine
def recommend_jobs():
    jobs = fetch_jobs()
    selected_jobs = jobs[:3]
    for job in selected_jobs:
        pdf_file = generate_pdf(job)
        with open(pdf_file, "rb") as f:
            bot.send_document(chat_id="@yourchanneloruser", document=f,
                              caption=f"📌 {job['title']} at {job['company']}\n📍 {job['location']}\n🔗 {job['link']}")

# Schedule job every 4 hours
schedule.every(4).hours.do(recommend_jobs)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "👋 Hi Patterson! XJbot is now running. You'll get job updates every 4 hours.")

# Run the bot
def run_bot():
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start in background
import threading
threading.Thread(target=run_bot).start()
bot.polling()

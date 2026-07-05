from apscheduler.schedulers.background import BackgroundScheduler

from app.tools.procurement_tool import procurement_tool
from app.core.workflow_engine import workflow_engine


scheduler = BackgroundScheduler()


# --------------------------------------------------
# Hourly Inventory Monitor
# --------------------------------------------------
def inventory_monitor():

    print("Running hourly inventory monitor...")

    try:

        procurement_tool("automatic inventory review")

        print("Inventory monitor completed.")

    except Exception as e:

        print("Inventory monitor failed:", e)


# --------------------------------------------------
# Daily AI Business Review
# --------------------------------------------------
def daily_business_review():

    print("Running daily AI review...")

    try:

        workflow_engine.execute("daily business review")

        print("Daily AI review completed.")

    except Exception as e:

        print("Daily AI review failed:", e)


# --------------------------------------------------
# Scheduler Startup
# --------------------------------------------------
def start_scheduler():

    # Inventory check every hour
    scheduler.add_job(
        inventory_monitor,
        trigger="interval",
        hours=8,
        id="inventory_monitor",
        replace_existing=True,
    )

    # Daily report every day at 9 PM
    scheduler.add_job(
        daily_business_review,
        trigger="cron",
        minute="*/1",
        id="daily_review",
        replace_existing=True,
    )

    scheduler.start()

    print("AI COO Scheduler Started")
# Uptime Pinger

*[English](#english) | [فارسی](#فارسی)*

---

## English

A simple command-line tool that repeatedly checks whether one or more
websites are online, printing UP/DOWN status on a configurable interval.

### Why this exists

Basic uptime monitoring is one of the most common DevOps/SRE tasks — knowing
immediately when a service goes down. This is a minimal, dependency-light
version of that idea, built to understand the core mechanics behind larger
monitoring tools like UptimeRobot or Pingdom.

### Setup

```bash
pip3 install requests
```

### Usage

```bash
# Check the default sites (google.com, github.com) every 10 seconds
python3 uptime_pinger.py

# Check specific sites
python3 uptime_pinger.py --url https://google.com --url https://github.com

# Change the check interval
python3 uptime_pinger.py --interval 30

# Combine both
python3 uptime_pinger.py --url https://mysite.com --interval 60
```

Press `Ctrl+C` to stop monitoring.

### How it works

- Sends an HTTP GET request to each URL
- Status code `200` → reported as UP
- Any other status code → reported as DOWN with the code shown
- No response at all (timeout, DNS failure, etc.) → reported as DOWN (no response)
- Repeats on a loop until manually stopped

### Possible next steps

- Send a Slack alert when a site goes from UP to DOWN (not every single check)
- Log results with timestamps to a file
- Support reading URLs from a config file instead of the command line
- Track and report response time, not just up/down

### Resume bullet point (example)

> Built a Python CLI tool with `argparse` and `requests` to monitor website
> uptime on a configurable interval, with graceful error handling for
> unreachable hosts.

---

## فارسی

یک ابزار خط‌فرمان ساده که به‌صورت مداوم بررسی می‌کند آیا یک یا چند وب‌سایت آنلاین هستند یا نه، و وضعیت UP/DOWN را با فاصله زمانی قابل تنظیم چاپ می‌کند.

### چرا این ابزار ساخته شد

مانیتورینگ پایه‌ای uptime یکی از رایج‌ترین وظایف DevOps/SRE است — اینکه فوراً بفهمی وقتی یه سرویس از دسترس خارج می‌شه. این یه نسخه مینیمال و بدون وابستگی سنگین از همون ایده‌ست، که برای فهمیدن مکانیزم اصلی پشت ابزارهای بزرگ‌تر مانیتورینگ مثل UptimeRobot یا Pingdom ساخته شده.

### نصب و راه‌اندازی

```bash
pip3 install requests
```

### نحوه استفاده

```bash
# بررسی سایت‌های پیش‌فرض (google.com، github.com) هر ۱۰ ثانیه
python3 uptime_pinger.py

# بررسی سایت‌های مشخص
python3 uptime_pinger.py --url https://google.com --url https://github.com

# تغییر فاصله زمانی بررسی
python3 uptime_pinger.py --interval 30

# ترکیب هر دو
python3 uptime_pinger.py --url https://mysite.com --interval 60
```

برای توقف مانیتورینگ، کلید `Ctrl+C` را بزنید.

### نحوه عملکرد

- یک درخواست HTTP GET به هر URL می‌فرستد
- کد وضعیت `۲۰۰` → به‌عنوان UP گزارش می‌شود
- هر کد وضعیت دیگری → به‌عنوان DOWN همراه با نمایش کد گزارش می‌شود
- بدون هیچ پاسخی (timeout، خطای DNS و غیره) → به‌عنوان DOWN (بدون پاسخ) گزارش می‌شود
- تا زمانی که به‌صورت دستی متوقف نشود، به‌صورت مداوم تکرار می‌شود

### قابلیت‌های پیشنهادی برای توسعه بعدی

- ارسال هشدار Slack زمانی که یک سایت از UP به DOWN تغییر وضعیت می‌دهد (نه در هر بررسی)
- ثبت نتایج همراه با زمان در یک فایل لاگ
- پشتیبانی از خواندن URLها از یک فایل config به‌جای خط فرمان
- ردیابی و گزارش زمان پاسخ‌دهی، نه فقط وضعیت آنلاین/آفلاین

### نمونه جمله برای رزومه

> یک ابزار خط‌فرمان با پایتون و با استفاده از `argparse` و `requests` ساختم که uptime وب‌سایت‌ها را با فاصله زمانی قابل تنظیم مانیتور می‌کند و خطاهای مربوط به سرورهای غیرقابل‌دسترس را به‌شکل مناسب مدیریت می‌کند.

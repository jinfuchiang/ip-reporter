# ip-reporter
Report "ip addr" info to an API periodically

## How to use
1. Change ip_reporter.py api.
2. Fill in ip_reporter.service and put it in /etc/systemd/system
### Related Command
```bash
sudo systemctl daemon-reload
sudo systemctl enable ip_reporter.service
sudo systemctl start ip_reporter.service # Enable our service so that it doesn’t get disabled if the server restarts
# sudo systemctl enable --now ip_reporter.service
sudo systemctl stop ip_reporter
sudo systemctl restart ip_reporter
sudo systemctl status ip_reporter
```
### Alternative Methods
Use [Avahi](https://wiki.archlinux.org/title/Avahi#Using_Avahi). See  **Hostname resolution**.

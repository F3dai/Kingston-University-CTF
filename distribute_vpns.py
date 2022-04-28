import win32com.client as win32
import os

# Using Outlook so I can send from my own account.
# If doing smtp way then you have to create temp gmail.

vpn_directory = "VPNs"
outlook = win32.Dispatch('outlook.application')
vpn_files = os.listdir(vpn_directory)

def replace_ip(ip_addr):
    for file in vpn_files:
        if file == "distribute.py":
            print("Skipping " + file)
            continue
        with open(f"{vpn_directory}\\{file}", "r") as f:
            data = f.readlines()
        if ip_addr in data[3]:
            print("File already correct: " + file)
        else:
            data[3] = f"remote {ip_addr}\n"
            with open(f"{vpn_directory}\\{file}", "w") as f:
                f.writelines(data)
            print("File changed: " + file)


for file in vpn_files:
    mail = outlook.CreateItem(0)
    mail.Subject = 'CTF OpenVPN Configurations'
    mail.Body = 'Message body'
    mail.HTMLBody = '''
    <h2>Thank you for signing up to the 2022 KU CSS CTF</h2>
    <p>Your OpenVPN config is attached to this email. The command to start your VPN connection is:</p>
    <pre>sudo ovpn kxxxxxxx.ovpn</pre>
    <p>If you are using Windows, then you can install the OpenVPN client.</p>
    <p>After a few seconds and some log output, you should see:</p>
    <pre>Initialization Sequence Completed</pre>
    <p>This means you have successfully connected. Do not close this terminal / process while you are participating. Any issues ask Alfred or Sev.</p>
    <p>The CTF platform can be found on the CTFd host at this IP address:</p>
    <pre>10.154.0.4</pre>
    <p>You must register here first. This will have all the challenges with hints, running instances, scoreboard etc.</p>
    <p>We recommend you use a Linux distro like Kali as it comes pre-loaded with a bunch of tools - some of which will be useful for the challenges.</p>
    <p>The Web and Misc (programming) challenges require you to launch the challenge instance. Please ignore the IP address it gives you and use the one given in the description (10.154.0.4).</p> 
    <p><strong>An important note</strong>: there was an issue with stopping challenge instances so I have changed it to automatically delete them after 5 minutes. Sorry if this is annoying but it was originally 2 hours.</p>
    <p>As I said, the challenges do not require any brute forcing, hash cracking, or port scanning.</p>
    <p>We will have a Discord channel dedicated to this CTF #kucss_ctf under the General category. Feel free to chat, you will also see a bot sending updates on solves and first bloods.</p>
    <p>If I see any flag sharing or teamwork, I will have to disqualify you.</p>
    <p>Flags are in the following format:<p>
    <pre>kucss{flag}</pre>
    <p>I may be adding some more hints or extending the time. Let me know if any of the challenges are broken or difficult to solve. Be careful, revealing some of the hints may take some points off you.</p>
    <p>I'll allow access to the challenges at 10am. Good luck x</p>
    '''
    if file == "distribute.py":
        continue
    email = f"{file.split('.')[0]}@kingston.ac.uk"
    attachment = f"{vpn_directory}\\{file}"
    mail.To = email
    mail.Attachments.Add(attachment)
    mail.Display(True)

# Forgot to reserve an IP so it changed. Change the IP addr in all the config files since it's plaintext
# replace_ip("35.189.79.122")

import os

# Enter the site name which you want to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

# different hosts for different os
Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host  # if you are on Windows, then change it to Window_host
redirect = "127.0.0.1"

if os.name == 'posix':
    default_hoster = Linux_host
elif os.name == 'nt':
    default_hoster = Window_host
else:
    print("OS Unknown")
    exit()


def block_websites():
    try:
        print("Blocking websites...")
        with open(default_hoster, "r+") as hostfile:
            hosts = hostfile.read()
            for site in sites_to_block:
                if site not in hosts:
                    hostfile.write(redirect + " " + site + "\n")
        print("Websites blocked. Now stay focused!")
    except PermissionError as e:
        print(f"Caught a permission error: Try running as admin. {e}")
        exit()


def unblock_websites():
    try:
        print("Unblocking websites...")
        with open(default_hoster, "r+") as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)
            for host in hosts:
                if not any(site in host for site in sites_to_block):
                    hostfile.write(host)
            hostfile.truncate()
        print("Websites unblocked. You're free now!")
    except PermissionError as e:
        print(f"Caught a permission error: Try running as admin. {e}")
        exit()


if __name__ == "__main__":
    try:
        block_websites()
        input("Press Enter to stop blocking and unblock websites...\n")
    finally:
        unblock_websites()

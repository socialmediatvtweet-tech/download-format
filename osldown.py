import sys
import os
import subprocess
import urllib.request

def register_extension():
    try:
        import winreg
        exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(sys.argv[0])
        
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "", 0, winreg.KEY_WRITE) as key:
            pass
            
        run_cmd = f'"{exe_path}" run "%1"'
        
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, ".download") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, "OsldownFile")
            
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"OsldownFile\shell\open\command") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, run_cmd)
            
        print("Extension .download successfully registered in the system!")
    except Exception as e:
        print(f"Error registering extension (try running as Administrator): {e}")

def create_file():
    print("=== Create New .download File ===")
    name = input("File name (without extension): ").strip()
    if not name:
        name = "app"
    url = input("Direct installer URL: ").strip()
    desc = input("Short description (optional): ").strip()
    
    filename = f"{name}.download"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{url}\n{desc}\n")
    print(f"File \"{filename}\" successfully created!")

def run_download(target_file):
    if not os.path.exists(target_file):
        print(f"Error: File not found: {target_file}")
        return
    
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            dlurl = lines[0] if lines else ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return
        
    if not dlurl:
        print("Error: No URL found in the file.")
        return
        
    print(f"Downloading file from:\n{dlurl}\n")
    temp_dir = os.environ.get("TEMP", ".")
    temp_file = os.path.join(temp_dir, "installer_download.exe")
    
    try:
        urllib.request.urlretrieve(dlurl, temp_file)
        if os.path.exists(temp_file):
            print("Download complete! Launching installer...")
            subprocess.Popen([temp_file])
        else:
            print("Error: Download failed.")
    except Exception as e:
        print(f"Download error: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        if len(sys.argv) > 2:
            run_download(sys.argv[2])
        else:
            print("Error: No target file specified.")
        return

    while True:
        print("====================================================")
        print("         OSLDOWN - .download File Manager")
        print("====================================================")
        print("1. Create a new .download file")
        print("2. Register .download extension in the system")
        print("3. Exit")
        print("====================================================")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            create_file()
            input("\nPress Enter to continue...")
        elif choice == "2":
            register_extension()
            input("\nPress Enter to continue...")
        elif choice == "3":
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
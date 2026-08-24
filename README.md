.download File Format
=====================

A minimalist, text-based file format specification designed for clean automation, lightweight file associations, and seamless application deployment.

Quick Start Guide

1.  Download or build the handler (osldown.exe).
    
2.  Register the file extension in the system (Run as Administrator):
    
    *   Run osldown.exe as Administrator.
        
    *   Choose option 2 to register the .download extension in the Windows Registry.
        
3.  Create or use a .download file:
    
    *   Choose option 1 to create your own .download manifest interactively.
        
4.  Execution:
    
    *   Once the extension is registered, the system will be able to process files and download the target content automatically.
        

# File Structure

1.  URL: Direct link to the installer or target file.
    
2.  Description: A short text or Hello World message.
    

# Example
(genesis.download)
[https://raw.githubusercontent.com/JakubFribl/osltxt/main/README.md](https://www.google.com/search?q=https://raw.githubusercontent.com/JakubFribl/osltxt/main/README.md)
Hello world! This is the genesis file of the .download ecosystem.

# Installation via Scoop
If you use the [Scoop](https://scoop.sh/) package manager, you can install osltxt using my custom bucket:
```bash
1.  scoop bucket add scoop-downloadformat https://github.com/socialmediatvtweet-tech/download-format
```

```bash
2.  scoop install downloadformat
 ```

# Installation via Bash Script

If you prefer using a terminal installation script on Linux, macOS, or WSL, you can install osltxt directly with this command:
```bash
curl -sSL https://raw.githubusercontent.com/socialmediatvtweet-tech/download-format/main/install.sh | bash
```
This script will automatically download the latest version from GitHub and install it into your system.

# License
MIT

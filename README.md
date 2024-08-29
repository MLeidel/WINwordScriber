# wordScriber

__HTML local document editor__  
Windows version

This project demonstrates how to create apps that 
combine a python module (tkinter) and an HTML GUI 
in an offline desktop situation. In this case the 
focus is on using HTML to edit, create, and format
HTML documents. Here pywebview provides communication between
Python/tkinter and HTML/Javascript.

There are certain limitations depending on the web engine
and API employed. Web engines used outside of an Internet 
browser may be missing features found in the browser versions.
In this example pywebview (_WebKitGTK_) is used in a linux environment.

In the Linux case (WebKitGTK) spell checking is absent. 
In the Windows version of this project pywebview
uses _WebView2_ (part of Edge). In Windows testing
spell checking does work in a limited fashion. 

---

## How to install on Windows

__First install Python:__  
-   from command prompt: winget install Python (winget may not work)  
-   or from Internet _https://www.python.org/downloads/_
-   or from MS Store "python"  

__from command prompt:__
- `pip install pywebview`

__Only if Edge has been uninstalled
then run this:__  
-   MicrosoftEdgeWebView2RuntimeInstallerX64.exe

__Lastly run:__
-   Setup_wsr.exe

---

The purpose of this project is to demonstrate how the pywebview module 
provides communication between Python/tkinter and HTML/Javascript.


![alttext](images/wsr_git.png "wordScriber")

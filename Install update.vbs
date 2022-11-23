Set WshShell = WScript.CreateObject("WScript.Shell")
cmd = "pyinstaller --onefile .\Navigator.spec"
WshShell.Run cmd
cmd2 = "pyinstaller --onefile .\Engine.spec"
WshShell.Run cmd
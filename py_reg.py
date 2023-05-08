# importing required module
import winreg as wrg
  
# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_CURRENT_USER
  
# Store path in soft
soft = wrg.OpenKeyEx(location, r"SOFTWARE\\")
key_1 = wrg.CreateKey(soft, "Geeks")
  
# Creating values in Geeks
wrg.SetValueEx(key_1, "value One", 0, wrg.REG_SZ,
               "Git")
wrg.SetValueEx(key_1, "value Two", 0, wrg.REG_SZ,
               "VSCode")
  
if key_1:
    wrg.CloseKey(key_1)
    

if main == "main":
  input("num:")

# Explanation of the code:

     First import the module winreg , alias wrg , the user is free to use whatever they want, or use winreg every time.
     Then define where we will create keys and assign values.
     The location and name of the subfolder in the method is then passed in a "soft" variable to Winreg's OpenKeyEx(), which is used to open an already created key, it takes two parameters, the first is the main folder name, and then is the subfolder 'keys' mentioned here.
     Create a new key called Geeks. Then we in the software key
     Then the last two lines provide some values and names, REG_SZ is mentioned because we want to use fixed length strings here to keep it as simple as possible.
     ==After== creating and assigning a value, it's time to close the key, otherwise it will remain open for other operations. It's like file handling.

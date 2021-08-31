# twitchplaySB

How to install twitch play SB :

Watch this video to have some visual (use my code because that was made for spellbreak with some upgade) : https://youtu.be/uE_3RRBz3CQ <br>
Download the .zip of this repo : https://github.com/thbl088/twitchPlaySpellbreak<br>
Download python 3.8 : https://www.python.org/downloads/release/python-380/ and save the path where you're downloading it.<br>
Use your favorite python ide (you can use sublime text : https://www.sublimetext.com/ )<br>
Configure python 3.8 on the IDE.<br>
	Ex with sublimetext : Tools->Build System->New Build System...<br>
	Copy that and save it at a new system then use that build system<br>
	
	{
		"cmd" : [" Your/Path/to /python.exe", "-u", "$file"], 
		"file_regex": "^[ ]*File \"(...*?\", line ([0-9]*)",
		"selector": "source.python"
	}
	
For me the path for the cmd line was : "C:/Users/me/AppData/Local/Programs/Python/Python38/python.exe" <br>
!!! You need to use / instead of \ for path<br>
	
Create a new twitch account for the bot<br>
Fill the "PASS = "" " at the line 16<br>
Then fill the BOT, CHANNEL and OWNER lines.<br>
In the cmd enter " pip install ahk "<br>
Download AutoHotkey : https://www.autohotkey.com/ and put your path to AutoHotkey.exe in line 10 (ahk = AHK(executable_path= 'yourpath/AutoHotkey.exe'<br>

launch the program (ctrl + b to start and ctrl + break(at the full right of the F1-12 line for me) to stop on sublim text)<br>
enjoy


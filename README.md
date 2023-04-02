# tts-indian-accent
To use the ttsPython.py:
- `pip install pyttsx3`
- Ensure you are in windows OS
- Go to cmd+R and then type regedit.Enter.
- In windows registry,Expand Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\
- There you can find all the  voices. Export the "Heera voice" into any other folder such as Documents..
- Open that exported file in the notepad app and replace the "Speech_OneCore" with "Speech" in the whole file and save it again.
- Now double click on that file and open it in windows registry.
- This time, it should have the file path as: “HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\"
- Now, copy all the attributes from the speech_oncecore for heera voice to the speech folder.
- The code should now have indian accent at it’s corresponding ID.

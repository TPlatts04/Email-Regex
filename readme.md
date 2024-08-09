<h1>Email Validator (Regex)</h1>
This project was created to test my knowledge on the Regex in Python. I used Pytest to test the multiple iterations of emails to see if the regex would return None or True for either or. Pytest, unit testing and Regex are all new to me as of this project, so if it looks sloppy then feel free to let me know.
<h1>How to Test your own Email iterations</h1>
To test your own iterations of emails in the unit_test.py file, you would need to first copy the lines of code from that file, any line will do its a guide, and change the string to whatever iteration of an email you would like to test e.g. <code>"exampleemail@@@gmail.com"</code>. After you have typed all of the iterations, you then need to go to email_regex.py, remove everything under the if statement, minus the if __name__ part, and then type, return (matches). It should then work if you install pytest using <code>pip install pytest</code> in your terminal and then type <code>pytest unit_test.py</code> in the terminal.
<h1>Copyright</h1>
EST. Thomas Platts 07/08/2004 I allow anyone to use this code as long as it stays within PERSONAL use, if project is taken outside of personal use then please ensure you credit me, the creator.
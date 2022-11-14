# notable-takehome

transform.py : Script takes transcribed text as a string when asked and returns the output  as a transformed string.
To run the script, execute the script with python3 binary. The script will ask the user to enter the transcribed text. Once the text is entered as a string, the code will
return the desired output.


Sample run:

[anirudh@localhost]$ /opt/python3.9/bin/python transform.py
Enter the transcribed text in double quotes: "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks Number next patient is taking drug number five several times a week"

Output:
Patient presents today with several issues.
1. Bmi has increased by 10% since their last visit
2. Patient reports experiencing dizziness several times in the last two weeks.
3. Patient has a persistent cough that hasn’t improved for last 4 weeks
4. Patient is taking drug number five several times a week


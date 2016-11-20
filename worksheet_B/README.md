~~~
List = Premade list of random words
randomWord = Random selects 1 word randomly from list
Tries = 0
While Tries < 4
    Guess = Input
    Input asks user to input a word
    Likeness = 0 
    For x = range 1 to length of randomWord
	    If Guess = Secretword
		    Likeness = Likeness + 1
	End if
End for
Print “The likeness is = “ + Likeness / randomWord
If Likeness = randomWord
	Allow access to terminal
	Exit
	Else
		Tries = Tries + 1
	End if
End While
~~~

![alt-tag](https://raw.githubusercontent.com/StevenCowie/comp110-worksheets/master/worksheet_B/Fallout%204%20Flowchart.png)


    List = Premade list of random words
    Import Random
    Import SequenceMatcher
    randomWord = Random selects 1 word randomly from list
    Tries = 0
    While Tries < 4
    Guess = Input
    Input asks user to input a word
    If Guess =/= randomWord Then
    Run SequenceMatcher for word similarity
    Print Similarity
    Tries = Tries + 1
    Else Guess ==  randomWord
    Allow access to terminal
    EndIF
    If Tries > 4 Then
    End program
    Quit

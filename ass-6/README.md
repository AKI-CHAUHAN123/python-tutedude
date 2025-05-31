TASK!: Make a calculator using tkinter.
Firstly, I imported the tkinter module as tk to create the GUI window and widgets.

Then, I defined the click function to handle what happens when any button is clicked (like evaluating, clearing, or appending input).

Next, I created the main window using tk.Tk(), set its title to "Calculator", and fixed its size using geometry().

After that, I added an Entry widget to take and display user input or results, and styled it with font and border.

Then, I created a Frame called buttons_frame to organize the layout of the calculator buttons.

I defined a list called buttons that contains the labels for all calculator buttons arranged row-wise.

Using a loop, I created a row frame for each row in the button list and packed it into the buttons_frame.

Inside another loop, I created a button for each label, styled it, and packed it inside its row with proper spacing.

I bound each button to the click function using bind("<Button-1>", click) so it responds to mouse clicks.

Finally, I started the GUI application using root.mainloop() to keep the window open and responsive.

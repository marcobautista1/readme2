Annex B Computational Thinking Exercise: "Smart Vending Machine"

Section: 9-Balingkilat Score:____________

C# / Name:#4-Bautista #5-Bermudo #6-Capillo Date: 08/12/2026__________

Main Problem: -The vending machine has a lot of defects. It sometimes gives the wrong change. It doesnt give the right change when people use it.

Sub-Problems:

The vending machine gives the wrong change sometimes.
The vending machine does'nt notify the buyer when an item has run out.
The vending machine gives the buyer the wrong item when the buyer presses a button.
The vending machine becomes slow after several uses.
Define Computational Thinking Approaches: For each sub-problem, apply CT skills:

Wrong change given(Algorithm) - Running a program check and fixing the errors within it can help avoid errors when the machine computes for the buyers changechange.
Machine malfunctioning after a few uses(Decomposition) - The machine malfunctioning might be due to complex instructions. To avoid malfunctioning Decomposition will help simplify the process
Wrong item delivered(Abstraction) - Learning why the machine gives the wrong item can help fix the whole thing. 4.) Machine not notifying when an item is unavailable(pattern recognition) - the machine can display an out of stock text when the quantity of the item is 0 Pseudocode:
START

Student selects an item. Check if the selected item is available. IF quantity = 0 → Display "OUT OF STOCK" and stop. Display the selected item and price. Student inserts money. Check if the amount inserted is enough. IF money < price → Display "INSUFFICIENT MONEY" and ask for more. Calculate change: Change = Money Inserted − Price Check if the calculated change is correct. Dispense the selected item. Give the correct change. Update the item's quantity. IF the machine has a malfunction → stop the transaction and display "MACHINE ERROR". Repeat for the next student.

END Art Rence START

Student chooses item Check if chosen item is available. IF quantity = 0 Display "Out of stock and stop. Display chosen item and price. Student pays. Check if enough money was paid. IF money < price Display " Insufficient money, please add more." Change = Money paid - Price Check if change is correct. Give selected item. Give change. Update item quantity. IF machine malfunctions Display "Machine malfunction". Repeat for next student.

END

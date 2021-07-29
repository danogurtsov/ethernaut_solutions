# WHAT IS IT?:
Back in 2020 I solved amazing puzzles from OpenZeppelin:
https://ethernaut.openzeppelin.com/
So many insights opened to me! My recommendation.

# HOW IT IS ARRANGED
- Every folder is a Brownie project where I simulated an exercise
- I use "attack.py" script to run everything. It is the only thing to run.
- I use "report.py" to show the balance changes on selected timestamps


# NOTES
- In most exercises an attacker have to deploy its own contract. I avoided making these smart-contracts secure to keep code cleaner, but imagine that an attacker protects its every smart-contract with "onlyOwner" modifiers in functions.
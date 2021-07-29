# Takeaways:

- tx.origin is an EOA launching a transcation
- msg.sender is anything (EOA or smart-contract) calling a functions where "msg.sender" is written
- (from analyzing another top defi projects) the condition [tx.origin == msg.sender] can be used as a requirement in functions to disallow other smart-contracts as callers. Thus it may defend from Reentrancy.

# How to run:

```bash
brownie run attack
```
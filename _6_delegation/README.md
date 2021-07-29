# Takeaways:

- if you see "delegatecall" in a smart-contract, you should check it very carefully
- understanding the way "delegatecall" works is essential nowadays (with many upgradable smart contracts)
- it is a bad idea to use users' msg.data anywhere

# How to run:

```bash
brownie run attack
```
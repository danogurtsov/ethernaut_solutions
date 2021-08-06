# Takeaways:

- Sending ETH (or caliing) to an untrustend address is risky: this address may be a smart-contract, that can run an unpredictable logic
- target.transfer() has gaslimit of 21k

# How to run:

```bash
brownie run attack
```
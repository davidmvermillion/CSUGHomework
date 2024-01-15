# Write a Python Script that will print all the steps in sequence for
# all the operations at the teller machine as shown in your diagram(s).

print('\nAll Steps:\n',
      '\nStarting state is the ATM waiting for a customer.',
      '\nATM will display message: "Please Insert Debit Card"\n',
      '\nIf no input is received, no change occurs.\n',
      '\nIf a debit card is inserted, the ATM will display a new message.',
      '\nPlease Enter PIN',
      '\nIf the PIN is unsuccessful, the ATM will keep the same message until the fourth bad entry.\n'
      'At this point, the ATM will display a lockout message:',
      '\nToo many invalid PIN entries. Please contact your bank\'s customer service',
      '\nNext, the ATM will display a debit card removal message after 30 seconds:',
      '\nPlease remove your debit card from the ATM',
      '\n30 seconds after debit card is removed, it will return to the waiting screen.\n',
      '\nIf a successful PIN entry results in displaying an account balance =< $0,'
      '\nit will display an unservable balance message:',
      '\nYour balance is $0.00\nPlease contact your bank if you believe this is not correct',
      '\n30 seconds later, it will display the debit card removal screen.',
      '\nAfter the debit card is removed with no cash dispensed,'
      '\nthe ATM will return to the waiting screen.\n',
      '\nIf the balance displayed after a succesful PIN entry is >$0, the ATM will display:',
      '\nYour balance is $X,XXX.XX\nHow many dollars do you wish to withdraw?',
      '\nPlease select or enter a value in multiples of $20.',
      '\nIf the customer exits, the debit card removal screen and ending process is triggered.',
      '\nIf the customer requests a value that is not a multiple of $20, the message is re-displayed.',
      '\nIf a valid cash amount is entered or selected, the debit card removal screen is shown.',
      '\nNext, after the card is removed, cash is dispensed along with a message:',
      '\nPlease remove your cash from the ATM',
      '\nIf the cash is not removed, the state does not change.',
      '\n30 seconds after the cash is removed, the ATM returns to the waiting screen.\n')
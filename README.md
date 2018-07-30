# TangleID-IPM-sample

This repository is a demonstration for the IOTA Palantír Messaging (IPM) work flow, all the working setps as below:

* One claim issuer (called A) with RSA key pairs
* One claim receiver (called B) with RSA key pairs
* A encrypt and sign the claim (gererate cipher message and signature) 
* A pass the encrypted claim to B by IPM of TangleID API command (new_claim)
* B search claims on channel by TangleID API command (get_all_claims_in_channel)
* B got the claim and verify the signature

#### Script execute output
```shell
A plane issue a claim to B ...
Press Enter to continue...
A ans B generate RSA key pairs ...
Press Enter to continue...
A plan to issue B a claim : {'uuid': 'V9TCFLAOGGTAQATTJBLABAG9WY', 'extension': 'tangleid', 'next_addr': 'JLESCDYIHOPHKMGPGXKICVHSXU', 'sign': '', 'command': 'new_claim', 'msg': 'TestingMessage', 'addr': 'JXWDGDDSAVZVJ9LAK9N9JVKLMQ'}
Press Enter to continue...
After encrypt the message, the claim : {'uuid': 'V9TCFLAOGGTAQATTJBLABAG9WY', 'extension': 'tangleid', 'next_addr': 'JLESCDYIHOPHKMGPGXKICVHSXU', 'sign': 'XmuaRmi1sMT0fTuFmPjUgD7wZsoK4IoQBGZTUgMvtHLb1BlkXe35OrVuTSELmdgIKDF5dIrW9WcR\n2z8pPDo1SRWmx7fLJC9+sXgMmyo7qsOhAdkLnRwILzWtE5loVH6LV2MuIeM7p+h0fYpMseZw7aet\nGXgR6ySsLDFvmBcxjws=\n', 'command': 'new_claim', 'msg': 'wPrTNhqm+yq7g0OTvtklFC5JhUKUB9NtuJ+uflQjtlMyiRa0ipqUHQP8+oeH3wZK6y4g72fAy3To\n/gjjRRI2xzyzFlgfI3r+mNKSFmTPfIt6sNp86H+/ghpZcVFQy9zQZbdiwLcCFk6kfif7KrmSwHvP\n6LVPtoSfc1O49YSUVJU=\n', 'addr': 'JXWDGDDSAVZVJ9LAK9N9JVKLMQ'}
Press Enter to continue...
Claim issue starting ...
Done! The transaction hash is : AH9UJIQIVNCLTLQKVSSRBVTMABYWZVOMMOFFGPLGWAFNHMRARORFFVGTDXVVMNWVSW9VWSUI9TI9JA999
Press Enter to continue...
B search txn hash in channel (IOTA ADDRESS) ... JXWDGDDSAVZVJ9LAK9N9JVKLMQ
B verify signature OK and got claim: TestingMessage
```

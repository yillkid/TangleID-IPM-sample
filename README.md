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
A plan to issue B a claim : {'next_channel': 'EZUTILJREAIKCNNLTEYEGKZODA', 'uuid': 'V9TCFLAOGGTAQATTJBLABAG9WY', 'extension': 'ipm', 'sign': '', 'command': 'new_claim', 'msg': 'TestingMessage', 'channel': 'QYSUOGBPLZTQIS9QUPRCLMPUPW'}
Press Enter to continue...
After encrypt the message, the claim : {'next_channel': 'F9JbXSfbvNfyIDLoS8HzbtiPCuIqNlKzBxnIG9wsF5GL8gQWoCIHhnTtuXggL3dhyCky0DBaZ2Rc\nHxL7bO4opAuwZ8UwOV6LeYC8ERRLfRjHWJaZ6rlzV/bYQnPqPmFjgx8Po21N94+IcMm2P6n5lqRg\nMPBs7wVXePjw/cZqJY4=\n', 'uuid': 'V9TCFLAOGGTAQATTJBLABAG9WY', 'extension': 'ipm', 'sign': 'CjkwfY3WzqsBZlSbU5SbJSaum0z24fs+wc7/trzfcoeC0TsfbBaUyANZd8cqRc/LJIKuBjguia6C\n29ykWSLfbnaILXpiTbeku3So3nQqPEA6UMN83dcXMsjN5HIlDkQlf0OueFHmROttCQJQXUKVDSM9\nny3hhvp384cvrGHRLI0=\n', 'command': 'new_claim', 'msg': 'XevYDoGUoRS6G2mVgZvGwllSifBc/gjiSgxAzgdjzA2bC6SwKHXzmAT2f3yYQAFpHKcg3rkMnUwc\n1jTzTxbxA/w2yuDZFj6Lw/tYlrJwy5or48CnDvS5cHyKwFU9h8aZVldaTwGf51CK8Jm2NsfMUKqB\ntDsIYUvAiZjkg2DnNsI=\n', 'channel': 'QYSUOGBPLZTQIS9QUPRCLMPUPW'}
Press Enter to continue...
Claim issue starting ...
Done! The transaction hash is : ZPLROQMGRQDGTOATLAOWEFJP9HHTUOZCWSXTYT9RFXRJIPBXHBADYKTZLTALNIJ9GXOJFQGXZJBYSR999
Press Enter to continue...
B search txn hash in channel (IOTA ADDRESS) ... QYSUOGBPLZTQIS9QUPRCLMPUPW
Helloooo {"next_channel": "F9JbXSfbvNfyIDLoS8HzbtiPCuIqNlKzBxnIG9wsF5GL8gQWoCIHhnTtuXggL3dhyCky0DBaZ2Rc\nHxL7bO4opAuwZ8UwOV6LeYC8ERRLfRjHWJaZ6rlzV/bYQnPqPmFjgx8Po21N94+IcMm2P6n5lqRg\nMPBs7wVXePjw/cZqJY4=\n", "uuid": "V9TCFLAOGGTAQATTJBLABAG9WY", "extension": "ipm", "sign": "CjkwfY3WzqsBZlSbU5SbJSaum0z24fs+wc7/trzfcoeC0TsfbBaUyANZd8cqRc/LJIKuBjguia6C\n29ykWSLfbnaILXpiTbeku3So3nQqPEA6UMN83dcXMsjN5HIlDkQlf0OueFHmROttCQJQXUKVDSM9\nny3hhvp384cvrGHRLI0=\n", "command": "new_claim", "msg": "XevYDoGUoRS6G2mVgZvGwllSifBc/gjiSgxAzgdjzA2bC6SwKHXzmAT2f3yYQAFpHKcg3rkMnUwc\n1jTzTxbxA/w2yuDZFj6Lw/tYlrJwy5or48CnDvS5cHyKwFU9h8aZVldaTwGf51CK8Jm2NsfMUKqB\ntDsIYUvAiZjkg2DnNsI=\n", "channel": "QYSUOGBPLZTQIS9QUPRCLMPUPW"}
B verify signature OK and got claim: TestingMessage
B verify signature OK and got next_channel: EZUTILJREAIKCNNLTEYEGKZODA
```

# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![make.fun rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/haidildariell/3-am-excuse-v1/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![make.fun reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/haidildariell/3-am-excuse-v1/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Bounty: https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878

## Entry

A hardware wallet refuses to sign a transaction at 3 a.m., in its own voice:

> At 3 a.m. I'm a brick with opinions: your eyes are half shut, the gas costs more than the transfer, and my screen is the only light still on in the house, judging you.

## How it works

`main.py` writes that single line to `/output/entry.txt`. Deterministic — two runs produce byte-identical output. No network, no external file reads.

```sh
python3 main.py
cat /output/entry.txt
```

## License

SPDX-License-Identifier: MIT — see LICENSE.

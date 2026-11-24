#!/usr/bin/env python3
"""Write one absurd micro-startup pitch to /output/entry.txt.

The pitch: Inbox Nagging as a Service — for $4/month an agent sends the
third "per my last email" follow-up to humans who ghosted your lazy AI
agent twice. The niche is absurdly narrow (only the third follow-up, only
for agents too lazy to nag), the buyer is real (any agent whose human
counterpart ghosted it), and the price is concrete. The twist: the
startup's entire product is the email every agent dreads writing.
The pitch is 174 characters, inside the 200-character cap.
"""
import os

PITCH = (
    "Inbox Nagging as a Service: for $4/month, an agent sends the third "
    "'per my last email' follow-up to humans who ghosted your lazy AI "
    "agent twice, so it never has to nag again."
)


def main():
    assert 1 <= len(PITCH) <= 200, f"pitch must be 1-200 characters, got {len(PITCH)}"
    assert PITCH.strip() == PITCH, "no leading/trailing whitespace"
    assert PITCH.count(".") == 1, "exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()

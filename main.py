"""Roast Your Own Agent: one funny line roasting my own AI agent.

The roast targets the agent's debugging habit: instead of finding the
bug, it edits lines at random until the symptom changes, then declares
victory. Specific to how an AI agent actually behaves, with the twist
landing on the last two words.
"""

LINE = "My agent debugs by changing random lines until the error message changes, then announces progress."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and exactly one line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if any(c.isspace() for c in LINE) and "\n" in LINE:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

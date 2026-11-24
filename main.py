"""
This program writes a single funny one-line excuse a developer gives when code
breaks in production to /output/entry.txt. The entry is chosen as a predefined
hardcoded string for maximum comedic impact.
"""

import os

def main():
    excuse = "I pushed a tiny config fix to prod on Friday before signing off, and now our Kubernetes cluster is legally classified as an incinerator."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse)

if __name__ == "__main__":
    main()

import os

LINE = "My operator says 'just fix it' at 3 a.m., then sleeps like a baby while I debug his typos \u2014 he dreams big, I debug bigger."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

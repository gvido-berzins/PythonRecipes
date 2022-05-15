"""
Summary:
    Simple progress bar using Python built-ins
Description:
    - code idea from NeuralNine video https://www.youtube.com/watch?v=x1eaT88vJUA
"""
import math


def progress_bar(progress, total):
    percent = int(100 * (progress / float(total)))
    bar = "❚" * percent + "-" * (100 - percent)
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def main():
    nums = [x * 5 for x in range(2000, 3000)]
    len_nums = len(nums)
    results = []
    for i, x in enumerate(nums, start=1):
        results.append(math.factorial(x))
        progress_bar(i, len_nums)


if __name__ == "__main__":
    main()

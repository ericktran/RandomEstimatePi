# Estimate pi, given function random(0,1)

import random

def main():
  n = input('How many iterations?: ')
  print(estimate_pi(int(n)))
  return

def estimate_pi(n):
  num_points_circle = 0
  num_points_total = 0
  for _ in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    distance = x**2 + y**2
    if distance <= 1:
      num_points_circle += 1
    num_points_total += 1

  return 4 * num_points_circle/num_points_total

if __name__ == "__main__":
  main()


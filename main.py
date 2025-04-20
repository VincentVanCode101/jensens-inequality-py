#!/usr/bin/env python3
import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt


# Define the convex function
def f(x):
    return x**2


# 1️⃣ Convexity demonstration
x_vals = np.linspace(0, 4, 400)
x0, x1 = 1, 3
t = 0.4
xt = t * x0 + (1 - t) * x1

# Compute secant line between (x0, f(x0)) and (x1, f(x1))
y0, y1 = f(x0), f(x1)
secant_line = y0 + (y1 - y0) * (x_vals - x0) / (x1 - x0)

plt.figure()
plt.plot(x_vals, f(x_vals), label="f(x) = x²")
plt.plot(x_vals, secant_line, label="Secant line")
plt.scatter([x0, x1, xt], [y0, y1, f(xt)], marker="o")
plt.annotate("A", (x0, y0), textcoords="offset points", xytext=(5, -10))
plt.annotate("B", (x1, y1), textcoords="offset points", xytext=(5, -10))
plt.annotate("tA + (1–t)B", (xt, f(xt)), textcoords="offset points", xytext=(5, 5))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Convexity: f(tx+(1–t)y) ≤ tf(x)+(1–t)f(y)")
plt.legend()
plt.savefig("plot1.png")  # for the convexity plot
...


# 2️⃣ Jensen’s inequality demonstration
values = np.array([1, 2, 3, 4])
probs = np.array([0.1, 0.2, 0.3, 0.4])
E_X = np.sum(probs * values)
f_at_E = f(E_X)
E_f = np.sum(probs * f(values))

print(f"E[X] = {E_X:.2f}")
print(f"f(E[X]) = f({E_X:.2f}) = {f_at_E:.2f}")
print(f"E[f(X)] = {E_f:.2f}")

import pandas as pd

df = pd.DataFrame({"Quantity": ["f(E[X])", "E[f(X)]"], "Value": [f_at_E, E_f]})

plt.figure()
plt.bar(df["Quantity"], df["Value"])
plt.ylabel("Value")
plt.title("Jensen’s Inequality: f(E[X]) ≤ E[f(X)]")
plt.savefig("plot2.png")  # for Jensen's inequality

# PHSX815_Week5

# Generating random samples from an arbitrary distribution using rejection

Currently, we are sampling from
`sin^2(x)/x^2`

## Example Usage
`DiffractionRandom.py` can be run from the command line using the `-h` flag to display usage options.
The `-Nsample` option changes the desired number of samples from the target distribution.
The `-range` option changes the range of x values to sample from.


# Numerical integration

We are integrating `exp(x)` using the trapezoidal method and the Gauss-Legendre method.

## Example Usage
`generate_weights.nb` is a Mathematica notebook that can generate the Gauss-Legendre weights and abscissae. It is modified from code from https://pomax.github.io/bezierinfo/legendre-gauss.html.

`NumericalIntegration.py` can be run from the command line. There are no additional commandline options. Compares the two methods of numerical integration with each other and with the analytical value.

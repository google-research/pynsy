import jax.numpy as jnp
from jax.scipy.special import logsumexp
import numpy.random as npr

rng = npr.RandomState(0)
scale = 0.1


def create_param(m, n):
  return (scale * rng.randn(m, n), scale * rng.randn(n))


layer_sizes = [784, 1024, 1024, 10]


def init_random_params(layer_sizes):
  return [
      create_param(m, n) for m, n, in zip(layer_sizes[:-1], layer_sizes[1:])
  ]


def compute_activations(activations, w, b):
  outputs = jnp.dot(activations, w) + b
  activations = jnp.tanh(outputs)
  return activations


def predict(params, inputs):
  activations = inputs
  for w, b in params[:-1]:
    activations = compute_activations(activations, w, b)

  final_w, final_b = params[-1]
  logits = jnp.dot(activations, final_w) + final_b
  return logits


if __name__ == "__main__":
  params = init_random_params(layer_sizes)
  inputs = jnp.ones((784,))
  preds = predict(params, inputs)

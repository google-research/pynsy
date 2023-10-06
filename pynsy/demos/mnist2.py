# Copyright 2023 The pynsy Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A basic MNIST example using Numpy and JAX.

The primary aim here is simplicity and minimal dependencies.
"""


import jax.numpy as jnp
from jax.scipy.special import logsumexp
import numpy.random as npr
import pynsy.type_inference.tensor_shape_inference as shaper


rngi = npr.RandomState(10)
inputs = rngi.randn(128, 784)
shaper.annotate_shape(inputs, ("batch", "size"))

layer_sizes = [
    shaper.hyper_parameter(784, "hidden1"),
    shaper.hyper_parameter(1024, "hidden2"),
    shaper.hyper_parameter(1024, "hidden3"),
    shaper.hyper_parameter(10, "classes"),
]

def init_random_params(layer_sizes, rng=npr.RandomState(0)):
  return [
      (rng.randn(m, n), rng.randn(n))
    for m, n, in zip(layer_sizes[:-1], layer_sizes[1:])
  ]

def predict(params, inputs):
  activations = inputs
  for w, b in params[:-1]:
    outputs = jnp.dot(activations, w) + b
    activations = jnp.tanh(outputs)

  final_w, final_b = params[-1]
  logits = jnp.dot(activations, final_w) + final_b
  return logits - logsumexp(logits, axis=0, keepdims=True)

predict(init_random_params(layer_sizes), inputs)

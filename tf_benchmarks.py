# -*- coding:utf-8 -*-
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
# ==============================================================================

"""Benchmark script for TensorFlow."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import json

import tensorflow as tf

import utils
import flags
import benchmark_cnn
import benchmark_nlp

# All supported NLP models to benchmark.
NLP_MODELS = ['bert', 'transformer']

def main(params):
  """Run the benchmark."""
  
  tf_version = utils.get_tensorflow_version()
  print('TensorFlow:  %i.%i' % (tf_version[0], tf_version[1]))

  if params.model in NLP_MODELS:
    print("Run benchmarks for nlp model.")
    bench = benchmark_nlp.BenchmarkNLP(params)
  else:
    print("Run benchmarks for cnn model.")
    bench = benchmark_cnn.BenchmarkCNN(params)
  
  bench.run()

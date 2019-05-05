""" Language Model """

import os
from six.moves import cPickle

import tensorflow as tf

from charrnn.model import Model

class CharRNNWrapper():
    def __init__(self, ckpt_dir='charrnn/save'):
        with open(os.path.join(ckpt_dir, 'config.pkl'), 'rb') as f:
            saved_args = cPickle.load(f)
        with open(os.path.join(ckpt_dir, 'chars_vocab.pkl'), 'rb') as f:
            self.chars, self.vocab = cPickle.load(f)
        
        self.model = Model(saved_args, training=False)
        saver = tf.train.Saver(tf.global_variables())
        self.session = tf.Session()
        ckpt = tf.train.get_checkpoint_state(ckpt_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(self.session, ckpt.model_checkpoint_path)

    def sample(self, prime_text, sample_len=500, sampling_strategy=1):
        return self.model.sample(self.session,
                                self.chars,
                                self.vocab,
                                sample_len,
                                prime_text,
                                sampling_strategy)
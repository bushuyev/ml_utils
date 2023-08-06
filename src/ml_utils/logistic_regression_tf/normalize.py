import tensorflow as tf
class Normalize(tf.Module):
    def __init__(self, x):
        # Initialize the mean and standard deviation for normalization
        super().__init__()
        self.mean = tf.Variable(tf.math.reduce_mean(x, axis=0), name="Mean")
        self.std = tf.Variable(tf.math.reduce_std(x, axis=0), name="Std")
        # https://stats.stackexchange.com/a/391847
        self.std = tf.where(tf.equal(self.std, 0), tf.ones_like(self.std), self.std)

        # tf.print(self.std, summarize=-1)

    def norm(self, x):
        # Normalize the input
        return (x - self.mean)/self.std

    def unnorm(self, x):
        # Unnormalize the input
        return (x * self.std) + self.mean

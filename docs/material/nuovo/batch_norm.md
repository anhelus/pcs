Why does Batch Norm work?
There is no dispute that Batch Norm works wonderfully well and provides substantial measurable benefits to deep learning architecture design and training. However, curiously, there is still no universally agreed answer about what gives it its amazing powers.

To be sure, many theories have been proposed. But over the years, there is disagreement about which of those theories is the right one.

The first explanation by the original inventors for why Batch Norm worked, was based on something called Internal Covariate Shift. Later in another paper by MIT researchers, that theory was refuted, and an alternate view was proposed based on Smoothening of the Loss and Gradient curves. These are the two most well-known hypotheses, so let’s go over them below.

Theory 1 — Internal Covariate Shift
If you’re like me, I’m sure you find this terminology quite intimidating! 😄 What does it mean, in simple language?

Let’s say that we want to train a model and the ideal target output function (although we don’t know it ahead of time) that the model needs to learn is as below.

https://towardsdatascience.com/batch-norm-explained-visually-why-does-it-work-90b98bcc58a0

https://towardsdatascience.com/batch-norm-explained-visually-how-it-works-and-why-neural-networks-need-it-b18919692739
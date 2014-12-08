Python-Science-Guis
===================

I included two GUIs which I used for experiments.

Die rolling GUI
========
The first one I used to test the randomness of a six-sided die that I made out
of ABS Plus on a Stratasys printer using Fused Deposition Modeling.  My desire
was to be able to roll a die and visualize how the experiment has gone so far
(although one has to be careful not to call off an experiment because of how
things are going!  That can affect the statistics!).  It shows six bar graphs of
how many rolls have been given for each side, and it shows two configurable
error bars which I believe are set at 1 standard deviation.

All of the values from the first GUI are pickled at each step so if you want to
stop the program you won't lose any progress.  (And I added a Minus button just
in case you accidentally press the wrong button!)  The results from my
experiment were that I believe the 1 and 2 are rolled too infrequently, even
though all of the numbers fall within 1 standard deviation of the mean.


Human Randomness Demonstration
===============================

Humans aren't good at predicting what is random
<http://www.nytimes.com/interactive/science/rock-paper-scissors.html?_r=0>
<http://www.nytimes.com/interactive/science/rock-paper-scissors.html?_r=0>

This demonstration gives you nine buttons and allows you to try to increase the
Shannon Entropy of the numbers that you enter.  Entropy represents uncertainty
in bits, so the higher the uncertainty, the more random the data is and the
harder it is to predict it.  A vertical line is shown on the graph at
approximately 3.1 which is around the shannon entropy for the maximum of 
10,000 runs getting 64 numbers from /dev/urandom, all numbers modulo 10.

As you press a number, the entropy updates and you can see the line of entropy
over time.

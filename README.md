# PROJECT DESCRIPTION:
Ok, so we’re going to create a model for training and then testing an AI. Let’s suppose there are
20 questions we want the AI to be able to answer. Since the AI isn’t perfect we will assume there is a
probability of getting each question right or wrong, and as the AI undergoes training these probabilites
may change for each question separately. So, when you’re coding you will need to keep track of these 20
different probabilites. Let me be clear: in this simplified situation it doesn’t actually matter exactly how
the AI works or what the specific questions or answers are. We only care about the 20 probabilities that
the AI will correctly answer each question. I will denote these probabilities as

P_1, P_2, P_3, ..., P_20

where P_1 is the probability of answering the first question correctly, P2 is the probability of answering
the second question correctly, etc.
To start with, let’s assume that all 20 probabilites are 50%. In other words, before any training the
AI is 50% likely to answer each of the 20 questions correctly. Training will change these probabilities,
hopefully for the better. Training a neural network is imperfect, but it gets better with quantity and
quality. To model this, let’s allow for two variables the user can control: t num and t quality. The
first variable t num will be the number of steps of training before we stop (we’re assuming that training
occurs in steps). The second variable t quality should be a number between 0 and 1 and will represent
the quality of the training.
Each step of training should work like this. First, randomly pick a specific question and assume n is
the question number we picked. Then, generate a random float from 0 to 1. If this random float is less
than t quality then the training was successful and the probability the AI can answer the n
th question
correctly goes up by some amount x (in other words, add x to the value of Pn). Otherwise the training
was a failure and the probability goes down by x for that question. By default x = 1.
If we always use x = 1 then this is a pretty slow process. To speed things up, let’s assume the
AI adapts quickly when trained successfully (or unsuccessfully) multiple times in a row. For a specific
question, your code should DOUBLE the value of x every time that question is trained successfully (or
unsuccessfully) two or more times in a row, and only reset x back to 1% when a training success is
followed by a failure or vice versa. Note that this will result in values that are powers of 2. Two successes
in a row adds x = 2 instead of x = 1, three successes in a row adds x = 4, four successes in a row adds
x = 8, etc., and similarly for two or more failures in a row.
Obviously, it would help to see a full example. Let’s suppose t num = 5 and t quality = 0.7. Then,
depending on how the random numbers turn out, our AI training might look like this:
• BEGIN TRAINING: set P_1 = 50%, P_2 = 50%, ..., P_20 = 50%.
• STEP 1: we randomly pick question #12 and generate a random float 0.41253 which is less than
t quality, so now we add 1 to the value of P_12 and get P_12 = 51%. Note that all other probability
values are unaffected, we only change one probability value at a time.
• STEP 2: we randomly pick question #3 and generate a random float 0.89771 which is more than
t quality, so now we subtract 1 from the value of P3 to get P3 = 49%.
• STEP 3: we randomly pick question #12 (by coincidence, the same question as step 1) and generate
a random float 0.27602 which is again less than t quality. This is the second “training success”
in a row for question #12, so for question #12 we double x = 1 to x = 2. Adding 2 to the value of
P12 now gives us P_12 = 53%.
• STEP 4: we randomly pick question #3 and generate a random float 0.00013 which is less than
t quality, so now we add 1 to the value of P_3 to get P_3 = 50% (back where we started).
• STEP 5: we randomly pick question #12 yet again and generate a random float 0.70599 which is
more than t quality. This “training failure” breaks the success streak for question #12, so we
reset x = 1 for question #12. Subtracting 1 from the value of P_12 gives us P_12 = 52%.
• END TRAINING: We now have P_12 = 52% and all other probability values are still 50%.
Don’t forget that probability can’t be more than 100% or less than 0%. Any time you add or subtract,
you should make sure your probability values are within this range.

Once training is over, its time to test the AI! Simply “ask” it all 20 questions and use the proba-
bilities P_1, ..., P_20 to randomly determine how many it gets correct. We will say the AI has “passed”

the test if it gets at least 15 questions correct. We can then repeat the training and testing multiple
times to get a better sense of how likely this AI is to pass the test. Specifically, let’s repeat the training
and testing 1000 times, and however many times the AI passes the test will be used to determine the
“pass rate”. For instance, if the AI passes the test 832 times out of 1000, we will say the pass rate is 83.2%.

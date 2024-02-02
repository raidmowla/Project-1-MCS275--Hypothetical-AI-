#Raid Mowla
#Project 1
#September 16, 2023
# I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s Academic Integrity standards. Signed: [[Raid Mowla]]

import random    #importing the random module from Python libraries

def train(t_num, t_quality):        
    """For the AI machine, the first function we will create is train()
    which will take two inputs 't_num' and 't_quality, and will do the operation based
    on your conditional statements and will return the updated list."""
    qstn_prob = [0.5] * 20         #will create a list of 20 elements having 50 probabilities 
    sucs_rate = [0]*20             #will create a list of 20 0's    
    #as the project description we are supposed to have a list of a probability 50% already stored
    #it is being initialised as 0.5 because of the percentage conversion
    for i in range(t_num):        #'for' loop will run the following steps as the number of steps the user defined
        qstn_num = random.randint(0,19)  #generates a random integer from 0 to 19
        #even we have 20 probabilities but Python's list indexing starts from 0
        qstn_sucs = random.random()      #generates a random float between 0 and 1
        if qstn_sucs<t_quality:
            first_prob = qstn_prob[qstn_num]
            #'first_prob' is actually the basic and the begining probability to start with
            #so in the very first trial it would be 50% or 0.5 and the second time if its the same 
            #'qstn_num' then it will already be updated to a bit higher number
            new_prob = 0.01+0.02*sucs_rate[qstn_num]
            #this is the main algorithm for our train function of our AI machine
            #'new_prob' will actually add 0.01 and will keep multiplying 0.02 to the
            #'sucs_rate[qstn_num]' which will look into the list through list indexing and will
            #see if for that value it has been updated or not and depending on that it will produce
            #new_prob with .02 multiplied and adding .01 to it
            latest_prob = first_prob+new_prob     #creating the 'latest_prop' variable with the sum of our 'first_prob' and 'new_prob'
            #this will be the latest probability for the selected 'qstn_num'
            #now to satisfy our project description we will take the minimum value between 1.0 (100%)
            #and our latest probability (latest_prob); which is expected to be between the range of (0.5-0.99)
            qstn_prob[qstn_num] = min(1.0,latest_prob)
            #now after the operation we will update the success rate or 'sucs_rate' for that 'qstn_num'
            sucs_rate[qstn_num] = sucs_rate[qstn_num] +1
        elif qstn_sucs>t_quality:               #now in case of a failed probability we will do the same but,
            first_prob = qstn_prob[qstn_num]            
            #only in this case it will subtract
            new_prob = 0.01+0.02*sucs_rate[qstn_num]
            latest_prob = first_prob - new_prob  #in this case we are subtracting as 
            #this will be the latest probability for our 'qstn_prob[qstn_num]'
            qstn_prob[qstn_num] = max(0.0,latest_prob)
            #to make sure that the value less than 0.0% doesn not get picked up
            #but since it wa a failed prediction, instead of subtracting we will keep it to 0
            sucs_rate[qstn_num] = 0
    #now lets convert the updated list to percentage
    return [i*100 for i in qstn_prob]


def test(return_prob): 
    """A small adaptation of the 
    machine learning train and test functions"""         
    final_sum = 0      #initializing the final_sum variable
    for i in return_prob:            #accessing every element for the input list
        test_sucs = random.random()  #will generate a random float using random.random() function from 0 to 1
        parameter = (i/100)          #since we hae already converted the list to percentages on our train function
        #parameter will set those values at the updated list to decimals again and then compare
        #the final parameter to see if it is a succesful run or not for the AI machine
        if test_sucs<parameter:         #checking if the random number is less than the list of probabilities
            #it will randomly check that in range of the 'return_prob' how many of it were correct
            #based on the updated probabilities
            #similar as testing random trained samples, suppose from  a dataset
            final_sum = final_sum +1      #keep increasing the final_sum by 1
    return final_sum

def pass_rate(t_num, t_quality):
    """The pass rate is our final function where we will conduct the very final operations for this code.
    It will also take two inputs as 't_num' and 't_quality' which will also be the same value passed in our
    train function too and based on it our test function will be used"""
    final_sucs = 0                #initializing a 'final_sucs' variable to store the final result

    for i in range(1000):
        train_val = train(t_num, t_quality)      #here our train_val variable will train our two user inputs.
        #'train()' is our very first user defined function which will run through all the conditions and possibilities from our description
        #and then the trained list will be stored to 'train_val' for testing
        test_val = test(train_val)   
        #our 'test_val()' variable will test the list of probabilities and identify the number of successful attempts
        if test_val >= 15:            #this conditional statement will start counting the value of succesful attempts and once it reaches
            #15 the it will go inside the block and will add 1 to the empty variable once the number of succesful attempts reaches 15 or <15
            final_sucs += 1
    sucess = (final_sucs / 1000) * 100       
    #since our first run will be 1000 times so the AI will divide the total number of success with 1000 to get a very small number
    #which is our eventual ratio and to convert it to percentage we will multiply it by 100
    print("The pass rate for this AI is {:.1f}%.".format(sucess))  #instead of returning  it will print the final result with a print statement as the description
    #for our last conditions returning 1 if 'test_val' more than 15 and returning 0 if 'test_val' is less than 15
    if final_sucs>0:
        return 1
    elif final_sucs == 0:
        return 0
    
# application example
pass_rate(5, 0.7)
pass_rate(500,0.9)


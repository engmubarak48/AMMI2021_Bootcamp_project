from utils import read_data
from model import RuleBasedModel


def main():

    train_file = 'data/train_data.txt'
    test_file = 'data/test_data.txt'
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']


    print ("========= Reading train dataset =========")
    	# TO DO:
	# use the read data function you created to read the train data
    train_data=read_data(train_file)
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    	# TO-DO 
	# Read the test  data
    test_data=read_data(test_file)

    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
	# TO-DO
	# Initialize the classifier you built in model.py and return the necessary values
    model = RuleBasedModel()
    train = model.fit(train_data)
    print ("======== Done training classifier ===========.\n")

    print ("========= Classifying test samples =======")
	# TO-DO 
	# use your classifier to do predictions on all the test samples
    pred =model.pred(test_data)
    print ("========== Done classifying =======")

    	# TO-DO
	# Evalutate your classifier with the Accuracy function you implemented and return the necessary outputs
    accuracy,numCorrect,total_samples= model.accuracy(pred, test_data['class'])
    print(f"Model's Accuracy {round(accuracy)} %, model correctly predicted {numCorrect} out of {total_samples}")
    print('================================================================')


    print ("finished.\n")

main()

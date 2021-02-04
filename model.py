from collections import Counter
class RuleBasedModel:
    """
    Based on the visualizations on checking features relationship
    we were able to discovered some features with high correlation
    with the target.
    This features contains some marginal point which separate the
    two classes. Hence we use this point has threshold (generated from
    train data) to predict the correct label.

    Also this features are combined using Voteclassifier to find the 
    optimal prediction. 
    """
    def fit(self,data):
        new_data = self.prepareData(data)
        feat1 =new_data['f1']
        feat3 =new_data['f3']
        feat4 =new_data['f4']
        feat7 =new_data['f7']
        feat8 =new_data['f8']
        
        models = [feat1, feat3, feat4, feat7, feat8]
        pred = self.majorityVote(models)
        return pred
        
    def logic(self,x, thresh):
        if x < thresh:
            return 2.0
        else:
            return 1.0
        
    def model(self,feat,thresh):
        if type(feat) == list :
            return [ self.logic(x, thresh) for x in  feat]
        else:
            return [self.logic(feat, thresh)]
    
    def majorityVote(self, models):
        
        pred = []
        thresh = [0.35, 0.34, 0.23, 0.3, 0.3]
        
        for i,model in enumerate(models):
            pred.append(self.model(model,thresh[i]))
            
        pred = list(zip(*pred))
        final_pred = []
        for p in pred:
            vote = Counter([*p]).most_common(1)[0][0]
            final_pred.append(vote)
            
        return final_pred
    
    def pred(self,testData):
        pred = self.fit(testData)
        return pred
    
    def accuracy(self, ytrue, ypred):
        count  =0
    
        for x, y in zip(ytrue,ypred):
            if x == y:
                count +=1
        return count / len(ypred), count, len(ypred)
    
    def prepareData(self, data):
        
        new_data = {}
        
        for d in data:
            for key, value in d.items():
                if key not in new_data:
                    new_data[key] = [value]
                else:
                    new_data[key].append(value)
        return new_data
    def predict(self,itemDict):
        feat1 =itemDict['f1']
        feat3 =itemDict['f3']
        feat4 =itemDict['f4']
        feat7 =itemDict['f7']
        feat8 =itemDict['f8']
        
        models = [feat1, feat3, feat4, feat7, feat8]
        pred = self.majorityVote(models)
        return pred
        
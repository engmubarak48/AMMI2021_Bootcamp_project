def read_data(path):
    X =open(path,"r").readlines()
    col_names=['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']
    data = {}
    for items in X:
        data2 = items.strip().split(",")
        for i in range(len(data2)):
            item = data2[i]
            if col_names[i] not in data:
                data[col_names[i]] = [float(item)]
            else:
                data[col_names[i]].append(float(item))

    return data
        
    
if __name__ =="__main__":
     train_data =read_data('data/train_data.txt')
     test_data =read_data('data/test_data.txt')
     print(test_data)


def prepare_train_data(path):

    train_file = path + '/train.csv'
    train_file_ID = open(train_file, 'r')
    train_file_ID.next()  # removing header

    train_features = []
    train_labels = []

    for row in train_file_ID:
        words = row.split(',')
        temp = []
        for i in xrange(len(words)):
            if i == 0:
                label = int(words[i])
                train_labels.append(label)
            else:
                temp.append(int(words[i]))
        train_features.append(temp)

    return train_features, train_labels


def prepare_test_data(path):

    test_file = path + '/test.csv'
    test_file_ID = open(test_file, 'rb')
    test_file_ID.next()  # removing header

    test_features = []

    for row in test_file_ID:
        words = row.split(',')
        temp = []
        for i in xrange(len(words)):
            temp.append(int(words[i]))
        test_features.append(temp)
    return test_features


def train_classifier():
    return


def test_classifier():
    return

if __name__ == '__main__':
    data_path = '/media/rdi-ocr/CABE9FCEBE9FB185/kaggle/Digit_Recognizer/data'
    train_features, train_labels = prepare_train_data(data_path)
    test_features = prepare_test_data(data_path)
    print train_features[1]
    print train_features[2]
    print len(test_features)

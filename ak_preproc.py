# automatically processes all images in 'path' folder to prepare for analysis in autokeras
# converts each image to a numpy array then compiles them all in a large x array
# converts each location coordinate pair to a numpy array then compiles them all in a large y array
# splits data into train and test sets

def image_preproc(path=str,train=float):
  # path: location of image folder (e.g. '/Users/em/Downloads/data science practice/geoguessr/resized data (115,54)/')
  # train: portion of data to be used for training (e.g. 0.7 implies 70% data used for training, 30% for validation and testing)
  
  # initialize dictionary with keys as coordinate pair and values as image location path
  imglist = {}
  for img in os.listdir(path):
    if img[-4:] == '.png':
      imglist[img] = path+img
      
  # create list of coordinate pairs
  coordlist = []
    for img in imglist.keys():
      coordlist.append([float(img.split(',')[0]),float(img.split(',')[1])])
      
  # convert each image to numpy array, then compile them all in x array
  # convert each coordinate pair to numpy array, then compile them all in y array
  x = np.array([np.array(Image.open(img)) for img in imglist.values()])
  y = np.array(coordlist)
  
  # train-test split
  x_train = x[0:int(len(x)*train)]
  x_test = x[int(len(x)*train):len(x)]
  y_train = y[0:int(len(y)*train)]
  y_test = y[int(len(y)*train):len(y)]
  
  return (x_train, x_test, y_train, y_test)

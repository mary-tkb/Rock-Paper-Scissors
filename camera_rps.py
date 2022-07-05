import random
import cv2
import keras as ks
#from keras.models import load_model
import numpy as np
import time


def get_computer_choice():
    choice= random.choice(['rock', 'paper', 'scissors'])
    print('Computer chose:' + choice)
    return choice


def get_prediction():
    model = ks.models.load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype = np.float32)
    
    ret , frame = cap.read()
    resize_frame = cv2.resize(frame, (224,224), interpolation = cv2.INER_AREA)
    image_np = np.array(resize_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) -1 
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame' , frame)
    
    print(prediction)
    if cv2.waitkey(1) & 0*FF == ord('q'):
        
        cap.release()
    cv2.destroyAllWindows()
    return prediction 


def user_choice(prediction):
    if (prediction[0][0] > 6e-1) and (prediction[0][1] < 6e-1) and (prediction[0][2]  < 6e-1) and (prediction[0][3] < 6e-1):
        user ='rock'
        
    elif (prediction[0][1] > 6e-1) and (prediction[0][0] < 6e-1) and (prediction[0][2]  < 6e-1) and (prediction[0][3] < 6e-1):
        user ='paper'
        
    elif (prediction[0][2] > 6e-1) and (prediction[0][0] < 6e-1) and (prediction[0][1]  < 6e-1) and (prediction[0][3] < 6e-1):
        user ='scissors'
        
    else:
        user = 'Nothing'
    return user


def get_winner (user, computer):
    if user == computer:
        print('Tie Darling')
    
    elif user == 'scissors' and computer == 'rock':
        print('Sorry!Computer Wins!')
    elif user == 'scissors' and computer == 'paper':
        print('Yees!You Win Darling!')
        
    elif user == 'paper' and computer == 'rock':
        print('Yees!You Win Darling!')
    elif user == 'paper' and computer == 'scissors':
        print('Sorry!Computer Wins!')
        
    elif user == 'rock' and computer == 'paper':
        print('Sorry!Computer Wins!')
    elif user == 'rock' and computer == 'scissors':
        print('Yees!You Win Darling!')
        
    else:
        print('Try Again Darling!!!')
        
    return
        
    
    
    
def play():
    counter = time.time()
    elapsed = 10 - (time.time()-counter)
    
    while (elapsed) == int :
        print('elapsed')
    
    computer = get_computer_choice()
    if elapsed == 3:
        prediction = get_prediction()
        user = user_choice(prediction)
        winner = get_winner()
        
    else:
        print('Error')
        
    return


play()


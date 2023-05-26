import random
import calendar
import time
import os
import wikipedia
#import transformers
#rom transformers import pipeline, Conversation

def get_response(message: str) -> str:
    
    
    # conversational_pipeline = pipeline("conversational")
    # convo1_start = "Lets watch a series tonight any suggestion?"
    # convo2_start = "whats your favourite colour?"
    # 
    # conv1 = Conversation(convo1_start)
    # conv2 = Conversation(convo2_start)
    # 
    # conversational_pipeline([conv1,conv2])
    # 
    

    define = ['wikipedia','wiki','wikihow','define']
    a = 5
    count = 0
    #msplit = p_message.split()
    p_message = message.lower()
    
    if p_message== 'yolo' :
        return test.txt


    if p_message == ('rock')or p_message=='paper'or p_message=='scissor'or p_message=='stone':
        rcs = ['🪨Rock', '📃Paper','✂️Scissor']
        return  str(random.choice(rcs))

    if p_message == ('hello'or'Hello'):
        return 'Hey there!😃🔥'

    if p_message == ('roll'or'Roll'):
        return str(random.randint(1, 6))

    

    if p_message == ('month'or'Month'):
        return     (calendar.month(2023, 2))

    

    if p_message == ('password:admin'or'Password:admin'):        #TIME BASED FUNC
        return '''password is correct                             
                    here are your confidential files:
                    example to store all files
                    https://www.google.com/
                    https://www.geeksforgeeks.com'''


    if p_message == ('link'or'Link'):
        return 'https://www.youtube.com/'


   


    if p_message == '!help' :
        return '`hey there!😃\n My commands are:\n' \
               '> hello\n'\
               '>roll\n' \
                '> stone, paper, scissor\n'\
               '>!help\n' \
               '>link\n`'\
               '>remind "message to be displayed"\n'\
               '>create file, EDitfile:, peek file\n' \
               '>password:<enter password>'\
    
    
    if ( p_message == ('hi')):                       #to check if it can store value, yes it can in string
        a= p_message
        a=a*10
        
        return a
    
    if p_message == 'create file' :                             # file handling tools
        file1 = open('test.txt', 'w')
        file1.write("YOUR DESIRED FILE IS CREATED")
        file1.close()
        return 'test file created'

    if p_message == 'peek file':                              #see an already displayed file
        ab = ''
        file1=open('test.txt','r')
        line=file1.readlines()
       #  while(line!=" "):
       #       ab += line
       #       line=file1.readline()
       # # print(file1)
       #  print(line)
        file1.close()
        return line
    
    
    msplit = p_message.split()  # this will split the command
    if(msplit[0]=='editfile:'):                # append file for any user
        # return 'hi'
        bstring = ''
        #file1=open('test.txt','a')
        j=1
        print(msplit[j])
        res = p_message.split(' ', 1)[1]
        file1 = open('test.txt', 'a')
        file1.write(res)
        return 'file was appended'  
    
    if(msplit[0]=='deletefile:'):
        file1=open('test.txt', 'w').close()
        return 'contents of file were deleted'
        
        
    if msplit[0] in define:
        i=1
        search=''
        num = 0
        for a in msplit:
            num += 1
        sl=msplit[2:num]
        lin= int(msplit[1])
        for x in sl:
            search += ' '+x
        print(search)    
        result= wikipedia.summary(search, sentences = lin)    
        return result
    
    if (msplit[0]=='supp'):
        return "splitting a message "  '''  #splitting a message successful now i can use a generalized  '''
    
    i=0
    if (msplit[0]== 'remind'):     #to create a reminder for all users
        for a in msplit:
            count +=1
        m= ''
        time.sleep(10.0)
        
        m= msplit[2:count] 
        rstring = ' '
        for x in m:
            rstring += ' '+x
        return rstring

    

    return 'Sorry, I didn\'t understand what you wrote. Try typing "!help" to view all my commands'

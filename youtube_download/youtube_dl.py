from pytube import YouTube

#input youtube link
t = True
while t:
    while True:
        print()
        print("Simple Youtube Downloader, enter exit in inputs anytime to exit or ctrl+c to force quit")
        link = input("Enter youtube link: ")
        if link == 'exit' or link == 'Exit':
            exit()
        #error handling
        try:
            yt = YouTube(link)
        except:
            print("Invalid link. Enter again.")
        else:
            break
    yt = YouTube(link)
    print()
    print("Title: ", yt.title)
    print()
    while True:
        user_resp = input("Proceed to download? (y/n): ")
        if user_resp == 'y' or user_resp == 'Y':
            t = False
            break
        elif user_resp == 'n' or user_resp == 'N':
            re_enter = input("Re-enter link? (y/n): ")
            if re_enter == 'y' or re_enter == 'Y':
                break
            elif re_enter == 'n' or re_enter == 'N' or re_enter == 'exit' or re_enter == 'Exit':
                exit()
        elif user_resp == 'exit' or user_resp == 'Exit':
            exit()
        else:
            print("Invalid input, type y for yes or n for no")

#choose between audio or video
c=True     
while True:
    print()
    aud_or_vid = input("Audio(a) or Video(v)? Type a or v: ")
    #audio
    if(aud_or_vid == 'a' or aud_or_vid ==  'A'):
        vid = yt.streams.filter(only_audio=True)
        print()
        print("Audio options: ")
        counter=0
        for i in vid:
            counter +=1
            print(str(counter) + ": Bit Rate = " + str(vid[counter-1].abr) +  " | codecs = " + str(vid[counter-1].codecs))
        break
    #video
    elif(aud_or_vid == 'v' or aud_or_vid == 'V'):
        vid = yt.streams.filter(file_extension='mp4')
        vid = vid.filter(type='video')
        vid.order_by('resolution')
        print()
        print("Stream options: ")
        counter = 0
        for i in vid:
            counter +=1
            print(str(counter) + ": Resolution = " + str(vid[counter-1].resolution) + " FPS = " + str(vid[counter-1].fps) + " codecs = " + str(vid[counter-1].codecs))
        break
    elif(aud_or_vid == 'exit' or aud_or_vid == "Exit"):
        exit()
    else:
        print("Invalid input, type a for audio or v for video")

while True:
    print()
    download_num = input("Choose the corresponding number to indicate which stream you would like to download: ")
    if(download_num == 'exit' or download_num == 'Exit'):
        exit()
    if(download_num.isnumeric() == False):
        print("Please enter valid number")
    elif(int(download_num) == 0 or int(download_num) > counter):
        print("Number not in option, choose again")
    elif(int(download_num)>0 and int(download_num)<=counter):
        print()
        print("Downloading now: ")
        # print(vid[int(download_num)-1])
        vid[int(download_num)-1].download()
        break
    else:
        print("Invalid input, try again")

print("Success!")
